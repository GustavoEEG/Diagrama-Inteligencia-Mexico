# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, los archivos de `data/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0 + Ola 1 + Ola 2** · corte de investigación: **19 de agosto de 2026**.

Tras la primera integración de Ola 2, el tablero contiene:

- 53 nodos;
- 71 relaciones;
- 32 fuentes registradas;
- 7 hipótesis de trabajo;
- escala epistemológica A–G;
- cronología ampliada 2018–2026.

La Ola 2 se documenta en [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md). Su hallazgo principal es **Juan Carlos de la Cruz Murillo como nodo puente corporativo** entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis Gas & Oil. El hallazgo no demuestra participación de Olán o de los López Beltrán en irregularidades de combustible.

## Estructura

```text
index.html
├── data/
│   ├── nodes.json
│   ├── edges.json
│   ├── sources.json
│   ├── hypotheses.json
│   └── timeline.json
├── research/
│   └── wave-02-amilcar-olan/
│       └── report.md
└── docs/
    ├── PROTOCOLO_MAESTRO.md
    └── methodology.md
```

`index.html` es el motor visual. El conocimiento se mantiene separado en JSON para que cada ola pueda ampliar o corregir el universo mediante pull requests pequeños y trazables.

## Principio central

**Una ruta entre nodos no demuestra culpabilidad, conocimiento, intención ni coordinación entre sus extremos.**

Las relaciones A–B forman el núcleo factual/documentado. C corresponde a información reportada o alegada. D–G contienen inferencias, hipótesis y wildcards que deben permanecer visual y metodológicamente separadas de los hechos.

El [`Protocolo Maestro`](docs/PROTOCOLO_MAESTRO.md) gobierna el proyecto completo. [`docs/methodology.md`](docs/methodology.md) conserva la versión metodológica inicial y puede seguir sirviendo como referencia compacta.

## Flujo de investigación

```text
investigación → fuentes → nodos → aristas → contradicciones → hipótesis → red team → PR → revisión → merge
```

Cada ola debe preferir una rama temática, por ejemplo:

- `agent/wave-02-amilcar-olan`
- `agent/wave-03-portacelis-ikon`
- `agent/wave-04-customs-navy`
- `agent/red-team-h01`

## Publicación

GitHub Pages debe estar configurado con:

- **Source:** `GitHub Actions`

El workflow `.github/workflows/deploy-pages.yml` se ejecuta en cada push a `main` y también puede lanzarse manualmente con `workflow_dispatch`.

Mantener el despliegue en Actions permitirá añadir validaciones automáticas antes de publicar, por ejemplo:

- JSON válido;
- IDs de nodos únicos;
- aristas sin nodos huérfanos;
- fuentes existentes para grados A–C;
- reglas especiales para hipótesis D–G;
- detección de duplicados y errores de cronología.
