# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

**Toda conversación nueva que continúe este proyecto debe leer primero ese protocolo y después consultar el estado actual de `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes.** Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0–13** · corte de investigación: **19 de agosto de 2026**.

Tras integrar la Ola 13, el universo esperado provisionalmente contiene:

- **137 nodos**;
- **235 relaciones**;
- **126 fuentes registradas**;
- **25 hipótesis de trabajo**;
- **12 overlays**;
- escala epistemológica A–G;
- análisis reproducible A–C vs A–G;
- control de baseline, tasa base, visibilidad y denominador;
- control explícito de **independencia de fuentes**;
- separación entre **existencia de un puente** y **significado causal/criminal del puente**;
- separación de **rol procesal/comercial** antes de inferir redes desde una causa penal;
- control de **recurrencia entre expedientes** sin asumir continuidad procesal;
- separación explícita entre **universo de inteligencia, acusación, imputación, proceso y condena**;
- modelado de sanciones/suspensiones por su **causal jurídica exacta**;
- separación de pistas de enforcement que comparten intermediario pero no transacción.

> Los conteos son verificados por Actions. Si difieren, prevalece `scripts/validate_graph.py`.

### Olas documentadas

- **Ola 2** — [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md): Juan Carlos de la Cruz Murillo como puente corporativo entre varias sociedades del universo de Amílcar Olán y la constitución inicial de Portacelis.
- **Ola 3** — [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md): continuidad operativa investigable y capa aduanal a operadores/patentes concretos.
- **Ola 4** — [`research/wave-04-portacelis-money-trail/report.md`](research/wave-04-portacelis-money-trail/report.md): money trail parcial y techo OSINT para beneficiario/control/pagos.
- **Ola 5** — [`research/wave-05-operation-files/report.md`](research/wave-05-operation-files/report.md): targets documentales RPC/SIGER, SENER, SAT Sector 13 y expediente del cateo a Ikon.
- **Ola 6** — [`research/wave-06-reverse-graph/report.md`](research/wave-06-reverse-graph/report.md): investigación inversa, centralidad y patente 3677 como puente investigativo.
- **Ola 7** — [`research/wave-07-customs-baseline/report.md`](research/wave-07-customs-baseline/report.md): grupo de control 3677/3830/3807; compartir agente no demuestra coordinación.
- **Ola 8** — [`research/wave-08-customs-denominator/report.md`](research/wave-08-customs-denominator/report.md): Full Portacelis Pediment Set no reconstruible con OSINT abierto; H13 estacionada y H14 formaliza sesgo de visibilidad/agregación.
- **Ola 9** — [`research/wave-09-femdo-353/report.md`](research/wave-09-femdo-353/report.md): autenticación del supuesto oficio FEMDO de 353 entidades. Resultado: autenticación parcial del contexto, no del documento; el lead permanece C. Se añade H16: republicación ≠ corroboración independiente.
- **Ola 10** — [`research/wave-10-identify-the-three/report.md`](research/wave-10-identify-the-three/report.md): intenta identificar las tres empresas no nombradas por FGR en los cateos FEMDO del 29 may 2026. El trío sigue sin identificar, pero Maquiladora de Lubricantes emerge como puente independiente entre Los Petrofactureros, Puerto Dos Bocas/Frontera y la causa penal 325/2025.
- **Ola 11** — [`research/wave-11-maquiladora-supply-chain/report.md`](research/wave-11-maquiladora-supply-chain/report.md): el proveedor concreto citado por la causa 325 no se identifica; se reconstruye un corredor independiente Galem↔Gutasa/Ecocarburante y Ecocarburante↔AIFA/Sedena↔Mefra/IPS. Nace H21: contaminación retrospectiva de contratos públicos.
- **Ola 12** — [`research/wave-12-extract-20-tomes/report.md`](research/wave-12-extract-20-tomes/report.md): identifica a **Karina Melissa Guerrero Rodríguez como proveedor histórico reportado de Maquiladora en 2020**, pero conserva abierta la identidad del proveedor específico al que alude la causa 325. Incorpora la carpeta `FED/TAM/REY/334/2021`, la rama Nexoil/Karina/Marvic y **Grupo Potesta** como nodo comercial-financiero reportado de la 325 con operaciones hacia **Vector Casa de Bolsa**. Se añaden H22 (recurrencia histórica) y H23 (proveedor histórico ≠ proveedor imputado sin documento puente).
- **Ola 13** — [`research/wave-13-potesta-vector-555/report.md`](research/wave-13-potesta-vector-555/report.md): somete a falsación la rama Potesta→Vector y el universo CFIC 555/108. Confirma actividad regulatoria real de Potesta, corrige su suspensión SAT de 2021 a causal IV por inactividad >12 meses, separa la pista FinCEN/opioides de la pista mexicana Potesta/huachicol y formaliza H24 (convergencia CFIC-108) y H25 (separación de pistas Vector).

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
│       ├── wave-09-femdo-353.json
│       ├── wave-10-identify-the-three.json
│       ├── wave-11-maquiladora-supply-chain.json
│       ├── wave-12-extract-20-tomes.json
│       ├── wave-12-vector-context.json
│       └── wave-13-potesta-vector-555.json
├── research/
│   └── wave-XX-*/
├── scripts/
│   ├── validate_graph.py
│   └── analyze_graph.py
└── docs/
    ├── PROTOCOLO_MAESTRO.md
    └── methodology.md
```

Los overlays son paquetes versionados. `data/manifest.json` define cuáles carga el tablero. Si un overlay contiene un `id` existente, actualiza ese objeto en tiempo de carga; IDs nuevos amplían el universo. `wave-12-vector-context.json` es un overlay técnico de contexto para materializar Vector como entidad referenciable; no representa una ola investigativa distinta.

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

Desde Ola 10:

```text
puente factual ≠ mando común
empresa presente en dos islas ≠ las islas son una sola red
prestación profesional ≠ conocimiento de la conducta del cliente
puerto Dos Bocas ≠ Refinería Dos Bocas
```

Desde Ola 11:

```text
misma causa penal ≠ mismo rol
empresa investigada ≠ proveedor ≠ cliente ≠ transportista ≠ contraparte ≠ simple mención
investigación posterior ≠ ilicitud retrospectiva de todos los contratos históricos
contrato público → suministro concreto → documento/lote → irregularidad → conocimiento
```

Desde Ola 12:

```text
recurrencia entre expedientes → mayor prioridad investigativa, no continuidad procesal automática
proveedor histórico ≠ proveedor citado por una causa posterior sin reconciliar fecha/CFDI/pedimento
lista de 555 ≠ lista de 353 hasta obtener ambos universos y cruzarlos nominalmente
relación con intermediario financiero ≠ lavado probado en cada operación
```

Desde Ola 13:

```text
listado/análisis de inteligencia ≠ acusado ≠ imputado ≠ vinculado a proceso ≠ condenado
suspensión administrativa → modelar causal jurídica exacta antes de inferir significado
pistas de enforcement que comparten intermediario ≠ mismo esquema sin puente transaccional
permiso/actividad regulada real ≠ exculpación de todas las operaciones
```

La existencia de una conexión debe probarse por separado de la interpretación causal de esa conexión. En expedientes grandes, **primero se clasifica el rol de cada entidad y después se calcula o interpreta la red**.

## Flujo de investigación

```text
investigación → fuentes → independencia de fuentes → clasificación de rol → grafo A–C/A–G → puentes → red team/baseline → denominador/visibilidad → hipótesis → targets documentales → overlay → PR → validación → merge
```

## Validación y análisis automáticos

- `.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py`.
- `.github/workflows/analyze-graph.yml` ejecuta `scripts/analyze_graph.py` sobre A–C y A–G.
- `.github/workflows/deploy-pages.yml` publica GitHub Pages en cada push a `main`.
