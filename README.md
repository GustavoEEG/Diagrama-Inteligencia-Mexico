# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0 + Ola 1 + Ola 2 + Ola 3 + Ola 4 + Ola 5** · corte de investigación: **19 de agosto de 2026**.

Tras integrar la Ola 5, el universo esperado contiene:

- **75 nodos**;
- **108 relaciones**;
- **48 fuentes registradas**;
- **11 hipótesis de trabajo**;
- **3 overlays**;
- escala epistemológica A–G;
- cronología ampliada 2018–2026.

La Ola 2 se documenta en [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md). Su hallazgo principal fue **Juan Carlos de la Cruz Murillo como nodo puente corporativo** entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis Gas & Oil.

La Ola 3 se documenta en [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md). Identificó **continuidad operativa investigable** alrededor de la reconfiguración societaria de Portacelis y bajó la capa aduanal a operadores/patentes concretos, sin convertir la prestación profesional en sospecha.

La Ola 4 se documenta en [`research/wave-04-portacelis-money-trail/report.md`](research/wave-04-portacelis-money-trail/report.md). Cuantificó parte del comercio declarado y un tramo downstream Portacelis→Pacific Tamerlane→facturas Oxy, pero encontró un techo natural del OSINT para beneficiario controlador, poderes, pagos y cuentas. De ahí H10: **opacidad documental ≠ control oculto**.

La Ola 5 se documenta en [`research/wave-05-operation-files/report.md`](research/wave-05-operation-files/report.md) y su plan ejecutable en [`research/wave-05-operation-files/acquisition-plan.md`](research/wave-05-operation-files/acquisition-plan.md). Cambia el foco de “más nombres” a **adquisición de evidencia**: identifica el FME `N-2024071962` para consulta/certificación SIGER, corrobora el uso operativo del permiso SENER `1701C124002733` en rutas ferroviarias y marítimas, formaliza el expediente SAT Sector 13 como target y separa lo confirmado del cateo federal a Ikon de la afirmación todavía no corroborada por inventario de que se incautaron documentos de Portacelis.

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
│       ├── wave-03-portacelis-operators.json
│       ├── wave-04-portacelis-money-trail.json
│       └── wave-05-operation-files.json
├── research/
│   ├── wave-02-amilcar-olan/report.md
│   ├── wave-03-portacelis-operators/report.md
│   ├── wave-04-portacelis-money-trail/report.md
│   └── wave-05-operation-files/
│       ├── report.md
│       └── acquisition-plan.md
├── scripts/
│   └── validate_graph.py
└── docs/
    ├── PROTOCOLO_MAESTRO.md
    └── methodology.md
```

`index.html` es el motor visual. Las expansiones nuevas se almacenan preferentemente como **overlays versionados** en `data/waves/`. `data/manifest.json` indica qué paquetes debe cargar el tablero. Cuando un overlay contiene un objeto con un `id` ya existente, actualiza ese objeto en tiempo de carga; los IDs nuevos amplían el universo. El validador reproduce la misma lógica antes de permitir integración.

## Principio central

**Una ruta entre nodos no demuestra culpabilidad, conocimiento, intención ni coordinación entre sus extremos.**

Las relaciones A–B forman el núcleo factual/documentado. C corresponde a información reportada o alegada. D–G contienen inferencias, hipótesis y wildcards que deben permanecer visual y metodológicamente separadas de los hechos.

Un nodo con alta centralidad puede ser importante únicamente por su función profesional —contador, comisario, abogado, agente aduanal, transportista—. **Centralidad no equivale a sospecha.**

La Ola 4 añadió la regla: **la falta de evidencia en fuentes abiertas no es evidencia de conspiración**. La Ola 5 añade otra: **cada hipótesis importante debe señalar qué documentos podrían matarla** y registrar sus llaves de adquisición.

El [`Protocolo Maestro`](docs/PROTOCOLO_MAESTRO.md) gobierna el proyecto completo.

## Flujo de investigación

```text
investigación → fuentes → nodos → aristas → contradicciones → hipótesis → red team → targets documentales → overlay → PR → validación → merge
```

Ramas temáticas sugeridas:

- `agent/wave-05-operation-files`
- `agent/wave-06-customs-baseline`
- `agent/wave-07-us-enforcement`
- `agent/red-team-h08`

## Validación automática

`.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py` sobre PRs que modifican datos relevantes. El validador lee la base y todos los overlays declarados en `data/manifest.json` y comprueba JSON válido, IDs, nodos huérfanos, grados A–G, fuentes y estructura de hipótesis/cronología.

## Publicación

GitHub Pages está configurado con **Source: GitHub Actions**. `.github/workflows/deploy-pages.yml` se ejecuta en cada push a `main` y también puede lanzarse con `workflow_dispatch`.
