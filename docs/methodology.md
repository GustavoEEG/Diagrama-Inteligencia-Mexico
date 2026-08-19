# Metodología del Intelligence Link Analysis

## Objetivo

Construir un universo versionado de actores, organizaciones, empresas, eventos, proyectos, fuentes y relaciones que permita explorar conexiones conocidas y formular hipótesis sin confundirlas con hechos.

El grafo **no asigna culpabilidad por proximidad**. Una ruta A → B → C no implica que A conozca, controle, financie o participe en las actividades de C.

## Escala epistemológica A–G

| Grado | Significado | Criterio mínimo |
|---|---|---|
| A | Confirmado / primario | Documento oficial, registro primario, sentencia, acto administrativo, declaración directa verificable o hecho institucional no controvertido. |
| B | Fuertemente documentado | Varias fuentes confiables o investigación sustentada en documentación identificable. |
| C | Reportado / alegado | Investigación periodística, denuncia, testimonio o atribución aún no confirmada de forma independiente. |
| D | Inferido | Relación deducida de hechos distintos; debe explicitarse el razonamiento. |
| E | Hipótesis investigable | Conexión que generaría predicciones o evidencia verificable y puede intentarse falsar. |
| F | Conspirativo | Hipótesis que exige varios supuestos no demostrados; se conserva para explorar el espacio de posibilidades, nunca como hecho. |
| G | Wildcard | Asociación remota o anomalía preservada sin evidencia causal actual. |

## Tipos de nodo

- `person`: persona física.
- `org`: institución, partido, autoridad u organización.
- `company`: empresa o vehículo corporativo.
- `project`: obra, megaproyecto o infraestructura.
- `event`: captura, decomiso, decisión, publicación, muerte, fuga, revocación, etc.
- `concept`: ecosistema analítico (p. ej. huachicol fiscal), no una entidad jurídica.

## Regla de aristas

Cada arista debe contener:

- `id`: identificador estable.
- `a`, `b`: nodos extremos.
- `g`: grado A–G.
- `rel`: descripción corta de la relación.
- `why`: explicación de qué se sabe y, cuando proceda, qué **no** demuestra.
- `src`: fuentes que sostienen específicamente esa arista.

Las fuentes deben sostener la relación descrita; no basta con que mencionen a ambos actores por separado.

## Hipótesis

Toda hipótesis debe incluir como mínimo:

1. evidencia o patrón que la favorece;
2. evidencia o explicación alternativa que la debilita;
3. dato faltante que permitiría elevarla o reducirla;
4. aristas críticas de las que depende.

Una hipótesis puede sobrevivir en el sistema aunque sea improbable, siempre que permanezca explícitamente etiquetada y sea falsable.

## Olas de investigación

Cada ola debe entrar mediante un PR temático y preferentemente modificar datos, no el motor visual.

Formato recomendado:

1. definir pregunta de la ola;
2. ampliar universo de fuentes;
3. añadir nodos;
4. añadir o degradar/elevar aristas;
5. registrar contradicciones;
6. actualizar hipótesis afectadas;
7. documentar qué puentes quedan como prioridad para la siguiente ola.

Ejemplos de ramas:

- `agent/wave-02-amilcar-olan`
- `agent/wave-03-portacelis-ikon`
- `agent/wave-04-customs-navy`
- `agent/red-team-h01`

## Red team

El proyecto debe buscar activamente información que destruya sus propias hipótesis. Encontrar que una conexión no existe, que las fechas no coinciden o que una relación era meramente comercial es un resultado útil y debe registrarse.

## Principio de actualización

La confianza puede subir **o bajar** con nueva evidencia. Git conserva el historial de cuándo apareció una arista, qué fuente la sustentó y por qué cambió de grado.
