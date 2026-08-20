#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
errors = []


def load(name):
    path = DATA / name
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        errors.append(f"{name}: JSON inválido o ilegible: {exc}")
        return None


nodes = load("nodes.json")
edges = load("edges.json")
sources = load("sources.json")
hypotheses = load("hypotheses.json")
timeline = load("timeline.json")

if not isinstance(nodes, list): errors.append("nodes.json debe ser una lista")
if not isinstance(edges, list): errors.append("edges.json debe ser una lista")
if not isinstance(sources, dict): errors.append("sources.json debe ser un objeto")
if not isinstance(hypotheses, list): errors.append("hypotheses.json debe ser una lista")
if not isinstance(timeline, list): errors.append("timeline.json debe ser una lista")

nodes = nodes if isinstance(nodes, list) else []
edges = edges if isinstance(edges, list) else []
sources = sources if isinstance(sources, dict) else {}
hypotheses = hypotheses if isinstance(hypotheses, list) else []
timeline = timeline if isinstance(timeline, list) else []


def duplicates(values):
    seen, dup = set(), set()
    for value in values:
        if value in seen:
            dup.add(value)
        seen.add(value)
    return sorted(dup)

node_ids = [n.get("id") for n in nodes if isinstance(n, dict)]
edge_ids = [e.get("id") for e in edges if isinstance(e, dict)]

for item in duplicates(node_ids): errors.append(f"ID de nodo duplicado: {item}")
for item in duplicates(edge_ids): errors.append(f"ID de arista duplicado: {item}")

node_set = set(node_ids)
source_set = set(sources)
valid_types = {"person", "org", "company", "project", "event", "concept"}
valid_grades = set("ABCDEFG")

for i, node in enumerate(nodes):
    if not isinstance(node, dict):
        errors.append(f"nodes[{i}] no es objeto")
        continue
    for field in ("id", "label", "type", "desc"):
        if not node.get(field): errors.append(f"nodo {node.get('id', i)} sin {field}")
    if node.get("type") not in valid_types:
        errors.append(f"nodo {node.get('id')} tipo inválido: {node.get('type')}")
    for sid in node.get("src", []):
        if sid not in source_set: errors.append(f"nodo {node.get('id')} refiere fuente inexistente {sid}")

for i, edge in enumerate(edges):
    if not isinstance(edge, dict):
        errors.append(f"edges[{i}] no es objeto")
        continue
    eid = edge.get("id", f"edges[{i}]")
    for field in ("id", "a", "b", "g", "rel", "why"):
        if not edge.get(field): errors.append(f"arista {eid} sin {field}")
    if edge.get("a") not in node_set: errors.append(f"arista {eid}: nodo a inexistente {edge.get('a')}")
    if edge.get("b") not in node_set: errors.append(f"arista {eid}: nodo b inexistente {edge.get('b')}")
    if edge.get("g") not in valid_grades: errors.append(f"arista {eid}: grado inválido {edge.get('g')}")
    src = edge.get("src", [])
    if edge.get("g") in {"A", "B", "C"} and not src:
        errors.append(f"arista {eid}: grado {edge.get('g')} requiere fuente")
    for sid in src:
        if sid not in source_set: errors.append(f"arista {eid}: fuente inexistente {sid}")

for sid, source in sources.items():
    if not isinstance(source, dict):
        errors.append(f"fuente {sid} no es objeto")
        continue
    for field in ("t", "d", "u"):
        if not source.get(field): errors.append(f"fuente {sid} sin {field}")
    url = source.get("u", "")
    if url and not url.startswith(("https://", "http://")):
        errors.append(f"fuente {sid}: URL no válida")

for i, hyp in enumerate(hypotheses):
    if not isinstance(hyp, dict):
        errors.append(f"hypotheses[{i}] no es objeto")
        continue
    for field in ("id", "title", "level", "support", "against", "missing"):
        if not hyp.get(field): errors.append(f"hipótesis {hyp.get('id', i)} sin {field}")

for i, item in enumerate(timeline):
    if not (isinstance(item, list) and len(item) == 2 and all(isinstance(x, str) and x for x in item)):
        errors.append(f"timeline[{i}] debe ser [fecha, descripción]")

if errors:
    print("VALIDACIÓN FALLIDA")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDACIÓN OK")
print(f"- {len(nodes)} nodos")
print(f"- {len(edges)} aristas")
print(f"- {len(sources)} fuentes")
print(f"- {len(hypotheses)} hipótesis")
print(f"- {len(timeline)} eventos de cronología")
