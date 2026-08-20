# Ola 6 — Métricas de investigación inversa

**Corte del grafo analizado:** 19 de agosto de 2026  
**Universo de entrada:** 75 nodos / 108 aristas antes de integrar hallazgos de Ola 6.

Estas métricas se producen con `scripts/analyze_graph.py`. Son instrumentos de priorización, no puntuaciones de culpabilidad.

## Dos grafos distintos

El analizador calcula deliberadamente dos universos:

- **A–C:** hechos/documentación + información reportada/alegada. Es el universo principal para seleccionar blancos de investigación.
- **A–G:** incorpora inferencias, hipótesis, conspirativo y wildcards. Sirve para observar cómo la especulación cambia rutas y centralidad, pero no debe usarse sola para escoger culpables o afirmar conexiones.

## Núcleo A–C

- nodos activos: **75**
- aristas A–C: **104**
- componentes conectados: **1**

### Degree — principales nodos

| Rango | Nodo | Degree |
|---:|---|---:|
| 1 | Portacelis Gas & Oil | 21 |
| 2 | Juan Carlos de la Cruz Murillo | 8 |
| 3 | Amílcar Olán | 8 |
| 4 | Andrés M. López Beltrán | 7 |
| 5 | HUACHICOL FISCAL | 7 |
| 6 | AMLO | 6 |
| 7 | Brownsville GTR | 5 |
| 8 | Armando Carrillo Peregrino | 4 |
| 9 | SEMAR / Marina | 4 |
| 10 | MG Energy | 4 |

### Betweenness — principales nodos

| Rango | Nodo | Betweenness normalizada |
|---:|---|---:|
| 1 | Portacelis Gas & Oil | 0.662812 |
| 2 | Juan Carlos de la Cruz Murillo | 0.360336 |
| 3 | Amílcar Olán | 0.281450 |
| 4 | HUACHICOL FISCAL | 0.254661 |
| 5 | Andrés M. López Beltrán | 0.172427 |
| 6 | Permiso SENER 52.084 M L | 0.099263 |
| 7 | SEMAR / Marina | 0.098206 |
| 8 | AMLO | 0.093610 |
| 9 | Reconfiguración Portacelis | 0.062793 |
| 10 | Armando Carrillo Peregrino | 0.053684 |

## Advertencia de sesgo de construcción

Portacelis domina la centralidad porque las Olas 2–5 deliberadamente expandieron su vecindario documental, logístico y regulatorio. Esa centralidad contiene **sesgo endógeno del investigador**: el nodo que investigamos más recibe más aristas y puede volverse artificialmente central.

Por esa razón Ola 6 no seleccionó automáticamente a Portacelis como siguiente blanco. Se buscó un puente:

1. que conectara islas distintas;
2. que no hubiera sido elegido previamente como protagonista;
3. que existiera ya en el núcleo A–C;
4. que pudiera ser falsado mediante un baseline externo.

El candidato elegido fue **Juan Hermilo Chávez Rodríguez / patente 3677**.

## Rutas A–C relevantes

### Olán → huachicol

`Olán → Juan Carlos de la Cruz Murillo → Portacelis → HUACHICOL FISCAL`

Esta ruta no prueba participación criminal de Olán: cada salto conserva su propia semántica y grado.

### Portacelis → Ingemar

`Portacelis → Juan Hermilo Chávez / patente 3677 → Ingemar`

Ésta fue la ruta que detonó la investigación inversa. Antes de Ola 6 significaba únicamente **agente aduanal compartido**.

### Andy → huachicol en A–C

La ruta mínima calculada fue:

`Andy → AMLO → Rafael Ojeda → SEMAR → HUACHICOL FISCAL`

Es un ejemplo didáctico de por qué **shortest path no es prueba causal**. La ruta mezcla parentesco, jerarquía institucional y una institución con oficiales investigados. No acredita conocimiento, orden, beneficio ni coordinación de Andy.

## Qué ocurre al abrir A–G

Al incorporar D–G, el grafo contiene una arista F Andy→huachicol y, por definición, el shortest path pasa a ser directo.

Esto no significa que la evidencia haya mejorado: sólo demuestra que la capa especulativa puede alterar drásticamente métricas y rutas.

**Regla resultante:** toda métrica usada para seleccionar un blanco debe publicarse al menos en dos versiones: A–C y A–G, y el razonamiento debe explicar cuál arista especulativa cambia el resultado.

## Articulation points relevantes del núcleo A–C

Entre los puntos de articulación aparecen Portacelis, Juan Carlos de la Cruz Murillo, Amílcar Olán, Andy, el permiso SENER, la reconfiguración de Portacelis, Armando Carrillo, militarización de aduanas/puertos y Oxy Services.

Un articulation point significa que retirar ese nodo altera conectividad topológica. **No significa que el actor controle la red.** En un grafo de investigación, también puede ser el resultado de cómo se modelaron hechos y documentos.

## Resultado de selección

**Blanco de investigación inversa:** `juan_hermilo_chavez` / patente nacional `3677`.

Razones:

- Portacelis aparece usando 3677 en una operación ferroviaria por Nuevo Laredo.
- Ingemar aparece usando 3677 en una operación distinta por Nuevo Laredo.
- ANAM identifica a Juan Hermilo Chávez Rodríguez como titular activo de la patente nacional 3677.
- durante el cierre de Ola 6 se verificó que Chávez fue vinculado a proceso en 2026 dentro de la causa federal asociada a la presunta red ferroviaria de Ingemar;
- simultáneamente, muestras no energéticas muestran que 3677 presta servicios a clientes de otros sectores.

La última observación es tan importante como las anteriores: obliga a medir un **baseline profesional** antes de llamar “red” al solapamiento.
