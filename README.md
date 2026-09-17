# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## 🕸️ Abrir Intelligence Link Analysis

**GitHub Pages:** https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/

> La publicación se realiza mediante GitHub Actions desde `main`. Cada merge a la rama principal dispara el workflow de Pages y actualiza el tablero publicado.

## 📘 Antes de continuar una investigación

La fuente metodológica canónica es [`docs/PROTOCOLO_MAESTRO.md`](docs/PROTOCOLO_MAESTRO.md).

Toda conversación nueva debe leer primero ese protocolo y después consultar `main`, `data/manifest.json`, los paquetes de `data/waves/` y los PR recientes. Las conversaciones son sesiones temporales; el repositorio es la memoria persistente del proyecto.

## Estado vigente

**Ola 0–18** · corte de investigación: **16 de septiembre de 2026**.

Tras cargar la Ola 18, el universo esperado contiene:

- **191 nodos**;
- **315 relaciones**;
- **183 fuentes registradas**;
- **36 hipótesis de trabajo**;
- **17 overlays**;
- escala epistemológica A–G;
- análisis reproducible A–C vs A–G;
- baseline, tasa base, visibilidad y denominador;
- independencia y provenance de fuentes/listas;
- separación entre existencia de puente y significado causal/criminal;
- separación de rol procesal/comercial antes de interpretar redes;
- continuidad operacional ≠ continuidad ilícita;
- contrato presentado a regulador ≠ operación ejecutada;
- proveedor compartido ≠ coordinación entre clientes;
- proveedor de alta frecuencia → medir denominador antes de llamar anomalía;
- acusación/investigación/proceso ≠ condena;
- contraevidencia y derechos de réplica incorporados al mismo nivel de trazabilidad;
- **perjuicio fiscal → volumen inferido ≠ volumen medido por autoridad**;
- **agente repetido en dos causas ≠ clientes coordinados**;
- **función estatal explotada por fraude ≠ función estatal capturada** sin evidencia de colaboración/protección pública.

> Los conteos son verificados por Actions. Si difieren, prevalece `scripts/validate_graph.py`.

### Olas documentadas

- **Ola 2** — [`research/wave-02-amilcar-olan/report.md`](research/wave-02-amilcar-olan/report.md): Juan Carlos de la Cruz Murillo como puente corporativo del universo de Amílcar Olán y la constitución inicial de Portacelis.
- **Ola 3** — [`research/wave-03-portacelis-operators/report.md`](research/wave-03-portacelis-operators/report.md): continuidad operativa y patentes aduanales 3830/3807/3677; compartir agente no demuestra coordinación.
- **Ola 4** — [`research/wave-04-portacelis-money-trail/report.md`](research/wave-04-portacelis-money-trail/report.md): money trail parcial y techo OSINT para beneficiario/control/pagos.
- **Ola 5** — [`research/wave-05-operation-files/report.md`](research/wave-05-operation-files/report.md): targets RPC/SIGER, SENER, SAT Sector 13 y expediente Ikon.
- **Ola 6** — [`research/wave-06-reverse-graph/report.md`](research/wave-06-reverse-graph/report.md): investigación inversa, centralidad y patente 3677 como puente investigativo.
- **Ola 7** — [`research/wave-07-customs-baseline/report.md`](research/wave-07-customs-baseline/report.md): baseline de patentes 3677/3830/3807.
- **Ola 8** — [`research/wave-08-customs-denominator/report.md`](research/wave-08-customs-denominator/report.md): full pediment set no reconstruible con OSINT; muestra observable ≠ universo.
- **Ola 9** — [`research/wave-09-femdo-353/report.md`](research/wave-09-femdo-353/report.md): autenticación parcial del supuesto universo FEMDO-353; republicación ≠ corroboración.
- **Ola 10** — [`research/wave-10-identify-the-three/report.md`](research/wave-10-identify-the-three/report.md): Maquiladora de Lubricantes emerge como puente independiente entre varias islas y la causa 325/2025.
- **Ola 11** — [`research/wave-11-maquiladora-supply-chain/report.md`](research/wave-11-maquiladora-supply-chain/report.md): corredor Galem↔Gutasa/Ecocarburante y Ecocarburante↔AIFA/Sedena↔Mefra/IPS; investigación posterior no contamina contratos históricos.
- **Ola 12** — [`research/wave-12-extract-20-tomes/report.md`](research/wave-12-extract-20-tomes/report.md): Karina Guerrero como proveedor histórico reportado de Maquiladora; carpeta 334/2021 y rama Potesta→Vector.
- **Ola 13** — [`research/wave-13-potesta-vector-555/report.md`](research/wave-13-potesta-vector-555/report.md): falsación Potesta→Vector, causal de suspensión y separación de pistas financieras.
- **Ola 14** — [`research/wave-14-cross-list-intelligence/report.md`](research/wave-14-cross-list-intelligence/report.md): cruce 334×CFIC selecciona Energética Carvel por recurrencia multi-expediente independiente.
- **Ola 15** — [`research/wave-15-carvel-longitudinal/report.md`](research/wave-15-carvel-longitudinal/report.md): continuidad Carvel 2016–2026; operador, Porteadora y permisos reales; continuidad operacional ≠ continuidad ilícita.
- **Ola 16** — [`research/wave-16-carvel-us-mx-supply-chain/report.md`](research/wave-16-carvel-us-mx-supply-chain/report.md): SENER revela Vitol/L Energy, relación Karina↔L Energy y upstream multicanal; L Energy emerge como puente.
- **Ola 17** — [`research/wave-17-lenergy-cross-island-news-delta/report.md`](research/wave-17-lenergy-cross-island-news-delta/report.md): L Energy resulta proveedor de alta frecuencia; se incorpora L.E. International Fuel Supply y controles de mercado; el news-delta abre Portacelis SAT→FGR, Deer Park→Ingemar→Crismon y Farías→nombramientos/aduanas. FGR niega órdenes de aprehensión contra Andy y Olán al 16 sep.
- **Ola 18** — [`research/wave-18-portacelis-sat-pediments/report.md`](research/wave-18-portacelis-sat-pediments/report.md): reconstruye la declaratoria SAT de Portacelis como 139 pedimentos/834 mdp reportados, separa la estimación MCCI de ~83M L del dato primario, incorpora la vía independiente de controles volumétricos/CSD y revela un cuarteto aduanal (Juan Hermilo, Hantulio, Víctor Carretero y Carlos Cruz Lara). Nacen H34–H36 y la hipótesis de captura funcional queda formalizada como marco investigable, no conclusión.

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
│       ├── ...
│       ├── wave-16-carvel-us-mx-supply-chain.json
│       ├── wave-17-lenergy-cross-island-news-delta.json
│       └── wave-18-portacelis-sat-pediments.json
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

```text
coincidencia → baseline → tasa base → control por volumen → hipótesis de enriquecimiento
```

**Sin denominador no hay anomalía cuantitativa.**

Reglas acumuladas:

```text
muestra observable ≠ universo
shipment ≠ pedimento ≠ ferrotanque ≠ operación reconstruida
10 republicaciones de una exclusiva ≠ 10 fuentes independientes
puente factual ≠ mando común
misma causa penal ≠ mismo rol
recurrencia entre expedientes → prioridad, no continuidad procesal
listado de inteligencia ≠ acusado ≠ imputado ≠ vinculado ≠ condenado
suspensión administrativa → modelar causal jurídica exacta
continuidad operacional ≠ continuidad ilícita
contrato presentado a regulador ≠ operación ejecutada
proveedor compartido ≠ coordinación entre clientes
proveedor de alta frecuencia → denominador antes de anomalía
versión oficial posterior + contraevidencia → actualizar el estado, no conservar el rumor más dramático
perjuicio fiscal → volumen estimado ≠ medición física/autoridad
agente repetido en dos causas ≠ clientes coordinados
función estatal explotada por fraude ≠ captura estatal sin colaboración/protección demostrada
```

La existencia de una conexión debe probarse por separado de su interpretación causal. En expedientes grandes, primero se clasifica el rol de cada entidad y después se calcula o interpreta la red.

## Flujo de investigación

```text
investigación → fuentes → independencia → clasificación de rol → grafo A–C/A–G → puentes → red team/baseline → denominador → provenance → continuidad temporal → hipótesis → targets documentales → overlay → PR → validación → merge
```

## Validación y análisis automáticos

- `.github/workflows/validate-graph.yml` ejecuta `scripts/validate_graph.py`.
- `.github/workflows/analyze-graph.yml` ejecuta `scripts/analyze_graph.py` sobre A–C y A–G.
- `.github/workflows/deploy-pages.yml` publica GitHub Pages en cada push a `main`.
