# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, los archivos de `data/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado inicial

**Ola 0 + Ola 1** · corte semilla: **18 de agosto de 2026**.

El tablero inicial contiene:

- 35 nodos;
- 47 relaciones;
- 24 fuentes registradas;
- 5 hipótesis de trabajo;
- escala epistemológica A–G;
- cronología semilla 2018–2026.

> Estos conteos describen la semilla inicial y pueden quedar obsoletos. Para el estado vigente, consultar los JSON de `main`.

## Estructura

```text
index.html
├── data/
│   ├── nodes.json
│   ├── edges.json
│   ├── sources.json
│   ├── hypotheses.json
│   └── timeline.json
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

Mantener el despliegue en Actions nos permitirá añadir validaciones automáticas antes de publicar, por ejemplo:

- JSON válido;
- IDs de nodos únicos;
- aristas sin nodos huérfanos;
- fuentes existentes para grados A–C;
- reglas especiales para hipótesis D–G;
- detección de duplicados y errores de cronología.
