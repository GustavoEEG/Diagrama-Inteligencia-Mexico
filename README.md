# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0 + Ola 1 + Ola 2 + Ola 3 + Ola 4** · corte de investigación: **19 de agosto de 2026**.

Tras integrar la Ola 4, el universo esperado contiene:

- **70 nodos**;
- **99 relaciones**;
- **43 fuentes registradas**;
- **10 hipótesis de trabajo**;
- **2 overlays**;
- escala epistemológica A–G;
- cronología ampliada 2018–2026.

La Ola 2 se documenta en [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md). Su hallazgo principal fue **Juan Carlos de la Cruz Murillo como nodo puente corporativo** entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis Gas & Oil.

La Ola 3 se documenta en [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md). Identificó **continuidad operativa investigable** alrededor de la reconfiguración societaria de Portacelis y bajó la capa aduanal a operadores/patentes concretos, sin convertir la prestación profesional en sospecha.

La Ola 4 se documenta en [`research/wave-04-portacelis-money-trail/report.md`](research/wave-04-portacelis-money-trail/report.md). Su hallazgo principal es doble: (1) el money trail abierto permite cuantificar valor declarado y un tramo downstream Portacelis→Pacific Tamerlane→facturas Oxy; (2) la información capaz de resolver quién conservó el **control económico real** parece concentrarse en expedientes SENER/SAT/notariales/fiscales que no hemos obtenido íntegros. Por eso se incorpora H10: **techo de fuente abierta ≠ control oculto**.

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
│       └── wave-04-portacelis-money-trail.json
├── research/
│   ├── wave-02-amilcar-olan/report.md
│   ├── wave-03-portacelis-operators/report.md
│   └── wave-04-portacelis-money-trail/report.md
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

La Ola 4 añade una regla complementaria: **la falta de evidencia en fuentes abiertas no es evidencia de conspiración**. Cuando la normativa indica que el dato decisivo reside en expedientes no públicos, ese expediente se convierte en target documental.

El [`Protocolo Maestro`](docs/PROTOCOLO_MAESTRO.md) gobierna el proyecto completo.

## Flujo de investigación

```text
investigación → fuentes → nodos → aristas → contradicciones → hipótesis → red team → overlay → PR → validación → merge
```

Ramas temáticas sugeridas:

- `agent/wave-04-portacelis-money-trail`
- `agent/wave-05-regulatory-files`
- `agent/wave-06-customs-baseline`
- `agent/red-team-h08`

## Validación automática

`.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py` sobre PRs que modifican datos relevantes. El validador lee la base y todos los overlays declarados en `data/manifest.json` y comprueba JSON válido, IDs, nodos huérfanos, grados A–G, fuentes y estructura de hipótesis/cronología.

## Publicación

GitHub Pages está configurado con **Source: GitHub Actions**. `.github/workflows/deploy-pages.yml` se ejecuta en cada push a `main` y también puede lanzarse con `workflow_dispatch`.
