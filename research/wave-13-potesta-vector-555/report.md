# Ola 13 — Grupo Potesta / Vector / Extract the 555

**Corte:** 19 de agosto de 2026  
**Objetivo:** probar si la rama `Grupo Potesta → Vector` agrega un puente financiero fuerte a la causa 325/2025 y evaluar el universo CFIC de 555/108 sin confundir análisis de inteligencia con imputación.

## Resultado ejecutivo

La ola no encontró todavía el puente financiero transaccional que permitiría afirmar que las operaciones reportadas entre Grupo Potesta y Vector forman parte de un esquema de lavado ligado al huachicol. El dato público más específico sigue siendo una reconstrucción de *El Universal* que atribuye a la causa 325/2025 aproximadamente **220 millones de pesos de operaciones entre Potesta y Vector**. La publicación no aporta fechas, números de cuenta, instrumentos, beneficiarios ni transferencias individualizadas, y el lenguaje citado del expediente sobre posible ocultamiento es condicional. Por ello la relación permanece **C — reportada**, no se eleva a B/A y no se etiqueta como lavado probado.

En paralelo, el red-team encontró evidencia primaria que obliga a describir a Grupo Potesta como **participante regulado real del mercado**, no como empresa de papel por defecto: CRE/CNE le otorgó el permiso de comercialización `H/20025/COM/2017`; SENER la listó con el permiso de importación `1701C117009131` por hasta 60 millones de litros de diésel; y la SCJN documentó que Potesta, Marea Negra y Petroservicios Yucatán litigaron una política de almacenamiento mínimo, confirmando sus permisos sectoriales.

La suspensión del padrón de importadores de Potesta en julio de 2021 también se reinterpreta con precisión. El listado público la marca bajo **causal IV de la regla 1.3.3**, cuya razón es más de 12 meses sin operaciones de comercio exterior. Esa suspensión es un hecho administrativo relevante, pero no es evidencia de pedimentos clonados, falsedad documental o falta de infraestructura.

La segunda gran aportación es separar dos pistas de Vector que narrativamente podrían fusionarse por error:

1. **Pista mexicana:** la causa 325/2025, según publicación periodística, atribuye ~220 mdp de operaciones Potesta–Vector sin fechas públicas.
2. **Pista estadounidense:** FinCEN identificó oficialmente a Vector como institución de *primary money laundering concern* en conexión con tráfico ilícito de opioides, cárteles y pagos por precursores químicos.

No se identificó una cuenta, wire, beneficiario, operación bursátil o periodo que conecte ambas pistas. Se crea H25 precisamente para impedir que una acción oficial estadounidense sobre opioides se use como corroboración automática de una alegación mexicana sobre huachicol.

Finalmente, el universo CFIC se vuelve más útil: *El Universal* reporta que el documento de 11 de junio de 2025 detectó al menos **555 entidades**, pero distingue un subconjunto de **108 empresas resaltadas** por funciones dentro del mercado de combustibles y/o distintos tipos de irregularidad. Esta diferencia debe preservarse. “Estar entre 555” no equivale a “estar entre 108”; ninguna de las dos categorías equivale automáticamente a acusación, vinculación a proceso o condena.

## 1. Grupo Potesta: de “posible fachada” a empresa real con una historia regulatoria compleja

### 1.1 Permiso de comercialización

La SCJN, en el amparo en revisión 278/2021, identifica a Grupo Potesta como titular del permiso **H/20025/COM/2017**, otorgado el 12 de abril de 2017. La misma sentencia identifica como coquejosas a Marea Negra y Petroservicios Yucatán, cada una con permisos propios.

Esto no exculpa operaciones específicas posteriores, pero sí falsifica una simplificación: **Potesta no debe modelarse como empresa inexistente o puramente instrumental por el solo hecho de aparecer en una investigación posterior.**

### 1.2 Permiso de importación de diésel

SENER publicó a Grupo Potesta dentro de la relación de permisos vigentes de importación de diésel con:

- permiso: `1701C117009131`;
- producto: diésel;
- volumen máximo autorizado: **60,000,000 litros**;
- fecha de otorgamiento: 29 de mayo de 2017;
- vencimiento publicado: 29 de mayo de 2018.

El permiso acredita autorización regulatoria; no demuestra que todo el volumen se haya importado efectivamente ni que cualquier operación posterior fuera lícita.

### 1.3 Litigio de almacenamiento

La sentencia de la SCJN documenta que Potesta, Marea Negra y Petroservicios Yucatán promovieron amparo contra obligaciones vinculadas con política pública de almacenamiento mínimo de petrolíferos.

Metodológicamente esto es importante por dos razones:

- confirma que Potesta participaba en una controversia regulatoria sectorial real;
- demuestra por qué **co-litigar no debe utilizarse como vínculo criminal**. Varias empresas del mismo sector pueden impugnar una regulación por interés económico común sin constituir una red operativa.

No se agregan aristas criminales hacia Marea Negra ni Petroservicios Yucatán por ese hecho.

## 2. La suspensión de 2021: corregir la causal exacta

Un listado público derivado del padrón identifica a Grupo Potesta con suspensión total y causal:

> RGCE 1.3.3, fracción IV.

La causal IV corresponde a la ausencia de operaciones de comercio exterior durante más de doce meses. *La Jornada* corroboró específicamente en 2025 que Potesta estaba suspendida desde julio de 2021 por llevar más de doce meses sin realizar operaciones de comercio exterior.

Esto cambia el significado del nodo.

Antes, leer simplemente “suspendida del padrón” al lado de “huachicol” podía generar una asociación implícita:

`Suspensión SAT → irregularidad aduanera → fraude`

La evidencia disponible obliga a sustituirla por:

`Suspensión SAT → causal IV → inactividad >12 meses`

No se crea una arista `potesta_sat_susp_2021 → huachicol`.

### Regla metodológica nueva

**Una sanción o suspensión administrativa debe modelarse por la causal jurídica exacta, no por la paráfrasis del titular periodístico.**

## 3. Potesta → Vector: qué sabemos y qué no

La publicación de *El Universal* sobre la causa 325/2025 afirma que Grupo Potesta registró operaciones por aproximadamente **220 millones de pesos con Vector Casa de Bolsa**.

La misma reconstrucción describe anomalías atribuidas al expediente en ingresos, egresos y número de empleados de Potesta y cita lenguaje según el cual la empresa “podría” estar enviando recursos a otras entidades o países para pretender ocultarlos.

### Lo que sí entra al grafo

`Grupo Potesta -C→ Vector Casa de Bolsa`

**Relación:** ~220 mdp de operaciones reportadas en la causa.

### Lo que no entra

No se crea:

`Potesta → lavado`

ni:

`Vector → huachicol`

como aristas A/B/C derivadas exclusivamente de los 220 mdp.

### Lo que falta

Para convertir esta rama en un verdadero *money trail* necesitamos:

- fechas exactas;
- cuentas de origen/destino;
- folios de operaciones bursátiles;
- transferencias SPEI/SWIFT;
- instrumento comprado/vendido;
- beneficiario final;
- intermediarios;
- relación económica subyacente;
- reportes UIF/SAR/STR o peritajes;
- cualquier circularidad o retorno de recursos.

Sin esa granularidad, **220 mdp es un monto agregado reportado, no una tipología de lavado demostrada**.

## 4. Vector: dos pistas que deben permanecer separadas

### 4.1 FinCEN / opioides

El 25 de junio de 2025, FinCEN/Treasury identificó oficialmente a Vector, junto con otras instituciones mexicanas, como *primary money laundering concern* en conexión con **tráfico ilícito de opioides**.

Treasury describió, entre otros señalamientos:

- uso atribuido a operadores relacionados con cárteles mexicanos;
- transferencias relacionadas con precursores químicos;
- periodos históricos distintos.

La acción es primaria y grave. Pero **no menciona a Grupo Potesta en el material oficial incorporado en esta ola y no se presenta como investigación de huachicol fiscal**.

### 4.2 Intervención CNBV

El 26 de junio de 2025, CNBV decretó la intervención gerencial temporal de Vector con el objetivo declarado de proteger a inversionistas y acreedores ante las implicaciones de las medidas estadounidenses.

La intervención se registra como hecho A. No equivale por sí misma a una sentencia que pruebe cada acusación de FinCEN.

### 4.3 Revocación de licencia

El 17 de diciembre de 2025, CNBV informó que la autorización de Vector fue revocada **a petición voluntaria de la entidad** y declaró expresamente que la decisión no guardaba relación con las medidas de FinCEN.

Este punto se conserva como contraevidencia obligatoria. No debe narrarse:

`FinCEN → CNBV castigó retirando licencia`

porque la autoridad mexicana dijo lo contrario respecto de la revocación de diciembre.

## 5. 555 ≠ 108

La publicación que reproduce el análisis CFIC reporta:

- **≥555 entidades detectadas** desde 2021;
- un subconjunto de **108 empresas resaltadas**.

El documento descrito por el medio combina en el subconjunto actividades y problemas de naturaleza distinta:

- importación;
- exportación;
- comercialización;
- distribución;
- transporte;
- venta/adquisición;
- suspensión de padrones;
- falta de permisos;
- facturación/pedimentos inconsistentes;
- precios anómalos;
- otras irregularidades.

Por tanto, el nodo `cfic_108_subset` se trata como una **categoría de inteligencia heterogénea**, no como lista de 108 integrantes de una sola organización.

### Regla

`listado/análisis de inteligencia ≠ acusado ≠ imputado ≠ vinculado a proceso ≠ condenado`

## 6. Convergencia externa: al menos 12 nodos ya estaban en nuestro grafo

La muestra nominal publicada incluye al menos doce entidades/personas que este proyecto ya había construido por rutas independientes:

| Nodo existente | Cómo llegó originalmente al grafo |
|---|---|
| Grupo Potesta | causa 325 + permiso regulatorio |
| Gutasa | causa 325 + permisos |
| Ecocarburante | causa 325 + AIFA + Mefra/IPS |
| Galem Energy | red comercial reportada / IPS |
| IPS | permisos + Galem + Ecocarburante/Mefra |
| Maquiladora de Lubricantes | Petrofactureros + Dos Bocas + causas 334/325 |
| Marlaya | carpeta 334/2021 |
| Nexoil | carpeta 334/2021 |
| Vector Casa de Bolsa | contraparte Potesta |
| Marvic | carpeta 334/2021 / transporte |
| Karina Melissa Guerrero | proveedor histórico Maquiladora / 334 |
| Leonel Guadalupe Jiménez | transporte reportado / 334 |

Esto genera H24: **convergencia externa CFIC-108**.

Es una señal útil porque varios nodos no fueron añadidos originalmente a partir del documento CFIC. Sin embargo, no permite afirmar significancia estadística:

1. nuestro proyecto ya está sesgado hacia empresas de combustible;
2. el documento CFIC analiza justamente ese sector;
3. no tenemos el universo de control;
4. no tenemos el anexo primario completo;
5. la categoría de inclusión de cada nodo puede ser distinta.

Por tanto, la conclusión correcta es:

> “Existe una convergencia externa que aumenta el valor de información de estos nodos.”

No:

> “Doce de nuestras empresas fueron confirmadas como parte de una misma red criminal.”

## 7. H20 y H22

### H20 — columna vertebral multi-isla

Se fortalece moderadamente porque el universo CFIC vuelve a juntar desde una fuente externa nombres a los que llegamos por:

- contratos públicos;
- permisos;
- carpetas históricas;
- transporte;
- estructura societaria;
- macrocausa 325.

Pero todavía puede tratarse de un **ecosistema de contrapartes heterogéneas**, no de una estructura con mando único.

### H22 — consolidación histórica

Se fortalece también de manera moderada porque el reporte CFIC indica que el análisis rastrea entidades desde 2021 y la muestra incluye múltiples nodos de la carpeta `FED/TAM/REY/334/2021`.

Aun así, no localizamos un documento procesal que demuestre:

`334/2021 → acumulada formalmente → 325/2025`

Así que recurrencia histórica y continuidad procesal siguen siendo conceptos distintos.

## 8. H25 — separación de pistas Vector

H25 queda **fuertemente sustentada como red-team**:

**Pista A**  
`Potesta -C→ Vector`  
causa 325 / huachicol / ~220 mdp reportados

**Pista B**  
`FinCEN -A→ Vector`  
opioides / cárteles / precursores

El hecho de que ambas compartan el mismo intermediario financiero **no permite fusionarlas**.

Una convergencia real requeriría:

- mismas cuentas;
- mismas fechas;
- mismos beneficiarios;
- mismos instrumentos;
- mismos originadores/destinatarios;
- o una pieza oficial que enlace ambas investigaciones.

## 9. Jorge Bechara y accionistas

Fuentes periodísticas que citan registros judiciales/corporativos identifican a Jorge Bechara Estefan López entre accionistas de Potesta y reportan un amparo en 2025 ante una eventual orden de aprehensión.

El grafo lo conserva como C hasta obtener el asiento primario del RPC.

Además:

**amparo ≠ culpabilidad.**

Se registra como conducta procesal defensiva.

## 10. Lo que esta ola falsificó

Ola 13 debilitó o impidió cuatro narrativas fáciles:

1. **“Potesta era una empresa de papel.”**  
   No puede afirmarse: existen permisos primarios, autorización de importación y litigio regulatorio documentado.

2. **“SAT la suspendió por huachicol.”**  
   La causal disponible es inactividad >12 meses; no prueba huachicol.

3. **“Vector perdió la licencia por FinCEN.”**  
   CNBV declaró que la revocación fue voluntaria y no guardó relación con las medidas FinCEN.

4. **“La acusación de FinCEN prueba la rama Potesta/huachicol.”**  
   No: FinCEN describe opioides/cárteles/precursores; falta puente transaccional.

## 11. H01 Andy ↔ huachicol

**Sin avance material.**

La Ola 13 no encontró:

- transferencias Potesta→Andy;
- cuenta Vector de Andy;
- beneficiario final asociado;
- instrucción;
- firma;
- comunicación;
- propiedad;
- intervención regulatoria atribuible a Andy.

La convergencia CFIC y la rama financiera aparecen independientemente del núcleo López Beltrán.

## 12. Próxima agenda sugerida

La siguiente ola debería abandonar el monto agregado de 220 mdp hasta conseguir transacciones y utilizar el nuevo activo que sí tenemos: **el subconjunto CFIC de 108**.

Prioridad:

1. extraer la lista completa de 108 de la publicación/documentos disponibles;
2. normalizar nombres/RFC;
3. cruzarla contra nuestros 130 nodos;
4. clasificar cada coincidencia por rol;
5. identificar **nodos nuevos que aparezcan en dos o más investigaciones históricas independientes**;
6. buscar un puente transaccional real entre Potesta y Vector;
7. intentar obtener el documento CFIC primario del 11 jun 2025;
8. comparar nominalmente `CFIC-108`, `CFIC-555` y `FEMDO-353`, sin asumir que son universos equivalentes.

La pregunta de mayor valor de información para la siguiente ola es:

> **¿Qué entidades aparecen simultáneamente en los universos 108/555, 353 y en expedientes previos como 334/2021 sin haber sido seleccionadas originalmente por nuestro propio grafo?**

Ese cruce podría revelar puentes externos con menos sesgo de selección.
