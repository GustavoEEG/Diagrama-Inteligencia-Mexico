# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0 + Ola 1 + Ola 2 + Ola 3 + Ola 4 + Ola 5 + Ola 6 + Ola 7** · corte de investigación: **19 de agosto de 2026**.

Tras integrar la Ola 7, el universo esperado contiene:

- **84 nodos**;
- **122 relaciones**;
- **65 fuentes registradas**;
- **13 hipótesis de trabajo**;
- **5 overlays**;
- escala epistemológica A–G;
- cronología ampliada 2018–2026;
- análisis reproducible de degree, betweenness, articulation points, bridges y shortest paths;
- baseline/control group obligatorio para puentes profesionales recurrentes.

La Ola 2 se documenta en [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md). Identificó a **Juan Carlos de la Cruz Murillo** como nodo puente corporativo entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis Gas & Oil.

La Ola 3 se documenta en [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md). Identificó continuidad operativa investigable alrededor de la reconfiguración societaria de Portacelis y bajó la capa aduanal a operadores/patentes concretos, sin convertir la prestación profesional en sospecha.

La Ola 4 se documenta en [`research/wave-04-portacelis-money-trail/report.md`](research/wave-04-portacelis-money-trail/report.md). Cuantificó parte del comercio declarado y un tramo downstream Portacelis→Pacific Tamerlane→facturas Oxy, pero encontró un techo natural del OSINT para beneficiario controlador, poderes, pagos y cuentas. De ahí H10: **opacidad documental ≠ control oculto**.

La Ola 5 se documenta en [`research/wave-05-operation-files/report.md`](research/wave-05-operation-files/report.md) y su plan ejecutable en [`research/wave-05-operation-files/acquisition-plan.md`](research/wave-05-operation-files/acquisition-plan.md). Formaliza las llaves documentales RPC/SIGER, SENER, SAT Sector 13 y el expediente del cateo a Ikon.

La Ola 6 se documenta en [`research/wave-06-reverse-graph/report.md`](research/wave-06-reverse-graph/report.md), con métricas en [`research/wave-06-reverse-graph/metrics.md`](research/wave-06-reverse-graph/metrics.md). Introduce investigación inversa reproducible y selecciona como puente a **Juan Hermilo Chávez Rodríguez / patente 3677**. La patente aparece en operaciones separadas de Portacelis e Ingemar y su titular fue vinculado a proceso en 2026 dentro de la causa ferroviaria asociada a Ingemar; la imputación no convierte otros despachos en ilícitos.

La Ola 7 se documenta en [`research/wave-07-customs-baseline/report.md`](research/wave-07-customs-baseline/report.md). Construye un grupo de control con las patentes **3677, 3830 y 3807**. Las tres muestran actividad multisectorial, por lo que compartir agente se debilita como señal de coordinación. H09 —concentración comercial— se fortalece, H12 baja de intensidad y nace H13: una prueba futura de **enriquecimiento** que sólo podrá evaluarse cuando exista denominador real de clientes, pedimentos y cuota de mercado.

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
│       ├── wave-05-operation-files.json
│       ├── wave-06-reverse-graph.json
│       └── wave-07-customs-baseline.json
├── research/
│   ├── wave-02-amilcar-olan/report.md
│   ├── wave-03-portacelis-operators/report.md
│   ├── wave-04-portacelis-money-trail/report.md
│   ├── wave-05-operation-files/
│   │   ├── report.md
│   │   └── acquisition-plan.md
│   ├── wave-06-reverse-graph/
│   │   ├── report.md
│   │   └── metrics.md
│   └── wave-07-customs-baseline/
│       └── report.md
├── scripts/
│   ├── validate_graph.py
│   └── analyze_graph.py
└── docs/
    ├── PROTOCOLO_MAESTRO.md
    └── methodology.md
```

`index.html` es el motor visual. Las expansiones nuevas se almacenan preferentemente como **overlays versionados** en `data/waves/`. `data/manifest.json` indica qué paquetes debe cargar el tablero. Cuando un overlay contiene un objeto con un `id` ya existente, actualiza ese objeto en tiempo de carga; los IDs nuevos amplían el universo. El validador reproduce la misma lógica antes de permitir integración.

## Principios centrales

**Una ruta entre nodos no demuestra culpabilidad, conocimiento, intención ni coordinación entre sus extremos.** Las relaciones A–B forman el núcleo factual/documentado; C corresponde a información reportada o alegada; D–G contienen inferencias, hipótesis y wildcards.

Un nodo con alta centralidad puede ser importante únicamente por su función profesional. **Centralidad no equivale a sospecha.** Desde Ola 6, toda métrica relevante debe distinguir al menos núcleo **A–C** de universo **A–G** para mostrar cuánto cambia la topología al incorporar hipótesis.

La falta de evidencia abierta tampoco es evidencia de conspiración. Cada hipótesis importante debe señalar qué documentos o mediciones podrían matarla.

Desde Ola 7, todo puente recurrente de infraestructura profesional —agente aduanal, notario, abogado, banco, naviera o proveedor logístico— debe pasar por:

```text
coincidencia → baseline → tasa base → control por volumen → hipótesis de enriquecimiento
```

**Sin denominador no hay anomalía cuantitativa.**

## Flujo de investigación

```text
investigación → fuentes → grafo A–C/A–G → puentes → red team/baseline → nodos/aristas → hipótesis → targets documentales → overlay → PR → validación → merge
```

## Validación y análisis automáticos

- `.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py` y comprueba JSON, IDs, nodos huérfanos, grados A–G, fuentes y estructura de hipótesis/cronología.
- `.github/workflows/analyze-graph.yml` ejecuta `scripts/analyze_graph.py` y calcula degree, betweenness, articulation points, bridges y rutas sobre A–C y A–G.

## Publicación

GitHub Pages está configurado con **Source: GitHub Actions**. `.github/workflows/deploy-pages.yml` se ejecuta en cada push a `main` y también puede lanzarse con `workflow_dispatch`.
