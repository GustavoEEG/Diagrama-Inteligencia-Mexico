#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"JSON inválido {path.relative_to(ROOT)}: {exc}")


base = {
    "sources": "data/sources.json",
    "nodes": "data/nodes.json",
    "edges": "data/edges.json",
    "hypotheses": "data/hypotheses.json",
    "timeline": "data/timeline.json",
}
overlays = []
manifest_path = DATA / "manifest.json"
if manifest_path.exists():
    manifest = load(manifest_path)
    base.update(manifest.get("base", {}))
    overlays = manifest.get("overlays", [])
    if not isinstance(overlays, list):
        raise SystemExit("data/manifest.json: overlays debe ser una lista")

sources = load(ROOT / base["sources"])
nodes = load(ROOT / base["nodes"])
edges = load(ROOT / base["edges"])
hypotheses = load(ROOT / base["hypotheses"])
timeline = load(ROOT / base["timeline"])

if not isinstance(sources, dict):
    raise SystemExit("sources debe ser un objeto JSON")
for label, value in (("nodes", nodes), ("edges", edges), ("hypotheses", hypotheses), ("timeline", timeline)):
    if not isinstance(value, list):
        raise SystemExit(f"{label} debe ser una lista JSON")


def merge_by_id(base_items, incoming, label):
    merged = {}
    for item in base_items:
        item_id = item.get("id")
        if not item_id:
            raise SystemExit(f"{label}: elemento base sin id")
        if item_id in merged:
            raise SystemExit(f"{label}: id duplicado en base: {item_id}")
        merged[item_id] = item
    for item in incoming:
        item_id = item.get("id")
        if not item_id:
            raise SystemExit(f"{label}: elemento overlay sin id")
        merged[item_id] = {**merged.get(item_id, {}), **item}
    return list(merged.values())


for overlay_rel in overlays:
    overlay_path = ROOT / overlay_rel
    if not overlay_path.exists():
        raise SystemExit(f"Overlay inexistente: {overlay_rel}")
    wave = load(overlay_path)
    if not isinstance(wave, dict):
        raise SystemExit(f"Overlay {overlay_rel} debe ser un objeto JSON")
    wave_sources = wave.get("sources", {})
    if not isinstance(wave_sources, dict):
        raise SystemExit(f"Overlay {overlay_rel}: sources debe ser objeto")
    sources.update(wave_sources)
    nodes = merge_by_id(nodes, wave.get("nodes", []), "nodes")
    edges = merge_by_id(edges, wave.get("edges", []), "edges")
    hypotheses = merge_by_id(hypotheses, wave.get("hypotheses", []), "hypotheses")
    wave_timeline = wave.get("timeline", [])
    if not isinstance(wave_timeline, list):
        raise SystemExit(f"Overlay {overlay_rel}: timeline debe ser lista")
    timeline.extend(wave_timeline)


def unique_ids(items, label):
    seen = set()
    for item in items:
        item_id = item.get("id")
        if not item_id:
            raise SystemExit(f"{label}: elemento sin id")
        if item_id in seen:
            raise SystemExit(f"{label}: id duplicado {item_id}")
        seen.add(item_id)
    return seen


node_ids = unique_ids(nodes, "nodes")
unique_ids(edges, "edges")
unique_ids(hypotheses, "hypotheses")

grades = set("ABCDEFG")
valid_types = {"person", "org", "company", "project", "event", "concept"}

for source_id, source in sources.items():
    if not isinstance(source, dict):
        raise SystemExit(f"sources: {source_id} no es objeto")
    for field in ("t", "d", "u"):
        if not source.get(field):
            raise SystemExit(f"sources: {source_id} sin campo {field}")

for node in nodes:
    if node.get("type") not in valid_types:
        raise SystemExit(f"nodes: tipo inválido {node.get('type')} en {node['id']}")
    if not node.get("label"):
        raise SystemExit(f"nodes: {node['id']} sin label")
    for source_id in node.get("src", []):
        if source_id not in sources:
            raise SystemExit(f"nodes: {node['id']} referencia fuente inexistente {source_id}")

for edge in edges:
    if edge.get("a") not in node_ids or edge.get("b") not in node_ids:
        raise SystemExit(f"edges: {edge['id']} apunta a nodo inexistente ({edge.get('a')}, {edge.get('b')})")
    if edge.get("g") not in grades:
        raise SystemExit(f"edges: {edge['id']} tiene grado inválido {edge.get('g')}")
    if not edge.get("rel") or not edge.get("why"):
        raise SystemExit(f"edges: {edge['id']} necesita rel y why")
    edge_sources = edge.get("src", [])
    if edge.get("g") in {"A", "B", "C"} and not edge_sources:
        raise SystemExit(f"edges: {edge['id']} grado {edge['g']} necesita al menos una fuente")
    for source_id in edge_sources:
        if source_id not in sources:
            raise SystemExit(f"edges: {edge['id']} referencia fuente inexistente {source_id}")

for hypothesis in hypotheses:
    for field in ("title", "level", "support", "against", "missing"):
        if not hypothesis.get(field):
            raise SystemExit(f"hypotheses: {hypothesis['id']} sin campo {field}")

for index, entry in enumerate(timeline):
    if not isinstance(entry, list) or len(entry) != 2 or not all(isinstance(x, str) and x.strip() for x in entry):
        raise SystemExit(f"timeline: entrada inválida en posición {index}: {entry!r}")

print(
    f"OK · {len(nodes)} nodos · {len(edges)} aristas · "
    f"{len(sources)} fuentes · {len(hypotheses)} hipótesis · {len(overlays)} overlays"
)
