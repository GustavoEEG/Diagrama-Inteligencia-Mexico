# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0 + Ola 1 + Ola 2 + Ola 3** · corte de investigación: **19 de agosto de 2026**.

Tras integrar la Ola 3, el universo contiene:

- **63 nodos**;
- **88 relaciones**;
- **38 fuentes registradas**;
- **9 hipótesis de trabajo**;
- escala epistemológica A–G;
- cronología ampliada 2018–2026.

La Ola 2 se documenta en [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md). Su hallazgo principal fue **Juan Carlos de la Cruz Murillo como nodo puente corporativo** entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis Gas & Oil.

La Ola 3 se documenta en [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md). Su hallazgo principal es una **continuidad operativa investigable alrededor de la reconfiguración societaria de Portacelis** —poder otorgado a Armando Carrillo Peregrino seis días antes de la venta y permanencia de Jesús Medina Córdova— además de una capa aduanal concreta con patentes 3830, 3807 y 3677. Ninguno de estos hallazgos demuestra por sí solo beneficiario final oculto, coordinación criminal ni participación de los López Beltrán.

## Arquitectura del conocimiento

```text
index.html
├── data/
│   ├── manifest.json
│   ├── nodes.json                # base histórica consolidada hasta Ola 2
│   ├── edges.json
│   ├── sources.json
│   ├── hypotheses.json
│   ├── timeline.json
│   └── waves/
│       └── wave-03-portacelis-operators.json
├── research/
│   ├── wave-02-amilcar-olan/
│   │   └── report.md
│   └── wave-03-portacelis-operators/
│       └── report.md
├── scripts/
│   └── validate_graph.py
└── docs/
    ├── PROTOCOLO_MAESTRO.md
    └── methodology.md
```

`index.html` es el motor visual. A partir de la Ola 3, las expansiones nuevas se almacenan preferentemente como **overlays versionados** en `data/waves/`. `data/manifest.json` indica qué paquetes debe cargar el tablero. Esto permite que cada ola añada o actualice nodos, aristas, fuentes, hipótesis y cronología sin reescribir todo el corpus histórico.

Cuando un overlay contiene un objeto con un `id` ya existente, el overlay actualiza ese objeto en tiempo de carga; los objetos con IDs nuevos amplían el universo. El validador reproduce la misma lógica antes de permitir la integración.

## Principio central

**Una ruta entre nodos no demuestra culpabilidad, conocimiento, intención ni coordinación entre sus extremos.**

Las relaciones A–B forman el núcleo factual/documentado. C corresponde a información reportada o alegada. D–G contienen inferencias, hipótesis y wildcards que deben permanecer visual y metodológicamente separadas de los hechos.

Un nodo con alta centralidad puede ser importante únicamente por su función profesional —contador, comisario, abogado, agente aduanal, transportista—. **Centralidad no equivale a sospecha.**

El [`Protocolo Maestro`](docs/PROTOCOLO_MAESTRO.md) gobierna el proyecto completo. [`docs/methodology.md`](docs/methodology.md) conserva la versión metodológica inicial como referencia compacta.

## Flujo de investigación

```text
investigación → fuentes → nodos → aristas → contradicciones → hipótesis → red team → overlay → PR → validación → merge
```

Cada ola debe preferir una rama temática, por ejemplo:

- `agent/wave-03-portacelis-operators`
- `agent/wave-04-beneficial-owners-money-trail`
- `agent/wave-05-customs-baseline`
- `agent/red-team-h06`

## Validación automática

`.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py` sobre PRs que modifican datos/metodología relevante. El validador lee la base y todos los overlays declarados en `data/manifest.json` y comprueba, entre otras cosas:

- JSON válido;
- IDs únicos en el universo resultante;
- nodos y tipos válidos;
- aristas sin nodos huérfanos;
- grados A–G válidos;
- fuentes existentes para relaciones A–C;
- referencias de fuentes sin romper;
- campos obligatorios en hipótesis;
- cronología estructuralmente válida.

## Publicación

GitHub Pages debe estar configurado con:

- **Source:** `GitHub Actions`

El workflow `.github/workflows/deploy-pages.yml` se ejecuta en cada push a `main` y también puede lanzarse manualmente con `workflow_dispatch`.
