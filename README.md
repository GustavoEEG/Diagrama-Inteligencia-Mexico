# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0–9** · corte de investigación: **19 de agosto de 2026**.

Tras integrar la Ola 9, el universo esperado provisionalmente contiene:

- **97 nodos**;
- **148 relaciones**;
- **80 fuentes registradas**;
- **16 hipótesis de trabajo**;
- **7 overlays**;
- escala epistemológica A–G;
- análisis reproducible A–C vs A–G;
- control de baseline, tasa base, visibilidad y denominador;
- control explícito de **independencia de fuentes** para filtraciones/exclusivas.

> Los conteos son verificados por Actions. Si difieren, prevalece `scripts/validate_graph.py`.

### Olas documentadas

- **Ola 2** — [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md): Juan Carlos de la Cruz Murillo como puente corporativo entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis.
- **Ola 3** — [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md): continuidad operativa investigable y capa aduanal a operadores/patentes concretos.
- **Ola 4** — [`research/wave-04-portacelis-money-trail/report.md`](research/wave-04-portacelis-money-trail/report.md): money trail parcial y techo OSINT para beneficiario/control/pagos.
- **Ola 5** — [`research/wave-05-operation-files/report.md`](research/wave-05-operation-files/report.md): targets documentales RPC/SIGER, SENER, SAT Sector 13 y expediente del cateo a Ikon.
- **Ola 6** — [`research/wave-06-reverse-graph/report.md`](research/wave-06-reverse-graph/report.md): investigación inversa, centralidad y patente 3677 como puente investigativo.
- **Ola 7** — [`research/wave-07-customs-baseline/report.md`](research/wave-07-customs-baseline/report.md): grupo de control 3677/3830/3807; compartir agente no demuestra coordinación.
- **Ola 8** — [`research/wave-08-customs-denominator/report.md`](research/wave-08-customs-denominator/report.md): Full Portacelis Pediment Set no reconstruible con OSINT abierto; H13 estacionada y H14 formaliza sesgo de visibilidad/agregación.
- **Ola 9** — [`research/wave-09-femdo-353/report.md`](research/wave-09-femdo-353/report.md): autenticación del supuesto oficio FEMDO de 353 entidades. **Resultado: autenticación parcial del contexto, no del documento; el lead permanece C.** Se añade H16: republicación ≠ corroboración independiente.

## Arquitectura del conocimiento

```text
index.html
├── data/
│   ├── manifest.json
│   ├── nodes.json
│   ├── edges.json
│   ├── sources.json
│   ├── hypotheses.json
│   ├── timeline.json
│   └── waves/
│       ├── wave-03-portacelis-operators.json
│       ├── wave-04-portacelis-money-trail.json
│       ├── wave-05-operation-files.json
│       ├── wave-06-reverse-graph.json
│       ├── wave-07-customs-baseline.json
│       ├── wave-08-customs-denominator.json
│       └── wave-09-femdo-353.json
├── research/
│   └── wave-XX-*/
├── scripts/
│   ├── validate_graph.py
│   └── analyze_graph.py
└── docs/
    ├── PROTOCOLO_MAESTRO.md
    └── methodology.md
```

Los overlays son paquetes versionados. `data/manifest.json` define cuáles carga el tablero. Si un overlay contiene un `id` existente, actualiza ese objeto en tiempo de carga; IDs nuevos amplían el universo.

## Principios centrales

**Una ruta entre nodos no demuestra culpabilidad, conocimiento, intención ni coordinación entre sus extremos.** A–B forman el núcleo factual/documentado; C es reportado/alegado; D–G son inferencias, hipótesis y wildcards.

**Centralidad no equivale a sospecha.** Toda métrica debe distinguir núcleo A–C de universo A–G.

**Falta de evidencia abierta ≠ evidencia de conspiración.** Cada hipótesis importante debe señalar qué documentos o mediciones podrían matarla.

Para puentes profesionales recurrentes:

```text
coincidencia → baseline → tasa base → control por volumen → hipótesis de enriquecimiento
```

**Sin denominador no hay anomalía cuantitativa.**

Desde Ola 8:

```text
muestra observable ≠ universo
shipment ≠ pedimento ≠ ferrotanque ≠ operación reconstruida
ausencia en una base ≠ ausencia en la realidad
```

Desde Ola 9:

```text
fuente originaria → republicaciones → corroboraciones independientes
10 republicaciones de una exclusiva ≠ 10 fuentes independientes
```

Una republicación sólo eleva confianza si aporta evidencia nueva: documento, expediente, entrevista propia, registro o confirmación institucional independiente.

## Flujo de investigación

```text
investigación → fuentes → independencia de fuentes → grafo A–C/A–G → puentes → red team/baseline → denominador/visibilidad → hipótesis → targets documentales → overlay → PR → validación → merge
```

## Validación y análisis automáticos

- `.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py`.
- `.github/workflows/analyze-graph.yml` ejecuta `scripts/analyze_graph.py` sobre A–C y A–G.
- `.github/workflows/deploy-pages.yml` publica GitHub Pages en cada push a `main`.
