# Ola 11 — Maquiladora Supply Chain / Extract 325

**Corte:** 19 de agosto de 2026

## Pregunta de investigación

La Ola 10 dejó a **Maquiladora de Lubricantes** como puente entre Los Petrofactureros, puertos de Tabasco y la causa penal 325/2025. La Ola 11 intenta responder una pregunta más estrecha y probatoria:

> **¿A quién compró Maquiladora el combustible que la causa 325/2025 cuestiona, y qué cadena comercial/logística conecta esas compras con las demás islas del grafo?**

La prioridad fue localizar la pieza judicial primaria de la causa 325/2025. No se obtuvo una copia pública de los tomos ni del anexo que nomine proveedores de Maquiladora. La investigación, por tanto, distingue entre lo que la prensa atribuye al expediente y las relaciones comerciales que pueden reconstruirse independientemente.

## Resultado principal

No se recuperó de forma reproducible el proveedor concreto de Maquiladora dentro de la causa 325/2025. **No se crea una arista Maquiladora→Galem, Gutasa o Ecocarburante.**

Sin embargo, la causa abre un corredor comercial independiente mucho más amplio:

```text
Causa 325/2025
├── Galem Energy (C, reportado por El Universal)
│   ├── Gutasa (C, red comercial reportada)
│   └── Ecocarburante (C, red comercial reportada)
│
└── Maquiladora de Lubricantes
    └── proveedor(es) no nominados públicamente → TARGET
```

Por otra vía documental/periodística independiente, **Ecocarburante** conecta con:

```text
Sedena / AIFA
Mefra Fletes
Impulsora de Productos Sustentables (IPS)
Miguel Castellanos Cruz
José Isabel Murguía Santiago
Matamoros 20-mar-2020
```

Esto transforma la causa 325/2025 en candidata a **columna vertebral comercial multi-isla**, pero no demuestra que todas las empresas que aparecen en ella formen una sola organización criminal.

## 1. Los 20 tomos existen como target real

La Jornada reportó el 23 de enero de 2026 que una jueza ordenó a FGR entregar a la defensa de Manuel Roberto Farías Laguna **los 20 tomos de la investigación** vinculada a la causa penal 325/2025, después de reclamos por acceso incompleto/testado.

Esto importa para el proyecto porque convierte una abstracción —“el expediente”— en un target documental de volumen y custodia concretos.

### Qué necesitamos extraer

Para cada empresa mencionada:

- hecho atribuido;
- fecha;
- contraparte;
- CFDI/factura;
- pedimento;
- permiso;
- monto/volumen;
- cuenta o forma de pago cuando exista;
- persona que firmó/representó;
- estatus procesal;
- evidencia exculpatoria o alternativa.

Sin esa matriz no debemos asumir que dos compañías mencionadas en la misma causa pertenecen a la misma célula.

## 2. Maquiladora: el proveedor sigue sin nombre

El Universal reporta que Maquiladora de Lubricantes aparece en la causa por **comprar combustible a una red de empresas señaladas de utilizar documentación falsa para ingresar hidrocarburos a México**.

La nota pública no identifica qué proveedor o proveedores realizaron esas ventas.

Por ello se crea el target:

`maquiladora_supplier_325_target`

Este target sólo podrá cerrarse con una pieza que individualice la operación: factura, CFDI, contrato, pedimento, declaración, dictamen o anexo judicial.

## 3. Galem, Gutasa y Ecocarburante: relación reportada dentro de la causa

El Universal atribuye a la causa 325/2025 que **Comercializadora de Combustible Gutasa** y **Ecocarburante** forman parte de la red comercial de **Galem Energy**.

La evidencia pública reproducida no incluye todavía el documento judicial que describa fechas, montos o naturaleza de esas operaciones. Por ello las aristas son **C — reportado**.

### Contraste regulatorio

La CRE registra:

- Gutasa — `H/21652/COM/2018`, comercialización de petrolíferos;
- Ecocarburante — `H/21910/COM/2018`, comercialización de petrolíferos.

SENER registró además para Gutasa el permiso de importación de diésel `1701C118001518` en 2018–2019.

Los permisos son evidencia de actividad regulada. **Tener un permiso no exculpa una operación irregular específica, pero tampoco convierte toda la actividad comercial en irregular.**

## 4. Ecocarburante → Sedena / AIFA

La ASF registra en la Cuenta Pública 2019 una adquisición de diésel para la construcción del AIFA en la que figura **Ecocarburante, S.A. de C.V.** como proveedor.

MCCI reconstruyó además contratos y documentos internos de mayor escala, incluyendo un contrato de hasta 496 millones de pesos para 27 millones de litros y una contratación posterior. La investigación documentó también incumplimientos de entrega.

La arista factual es:

`Sedena -A→ Ecocarburante -A→ AIFA`

La interpretación NO es:

`Sedena compró huachicol`.

Sedena sostuvo públicamente, en respuesta a la investigación de MCCI, que el contrato se celebró **con apego a la ley**. Esa postura entra al grafo como contraevidencia obligatoria.

## 5. Ecocarburante ↔ Mefra Fletes

MCCI documentó que **Miguel Castellanos Cruz** representó a Ecocarburante en el seguimiento del contrato con Sedena y también representó a **Mefra Fletes**.

La misma investigación reproduce información de un acta de inspección del **20 de marzo de 2020 en Matamoros**:

- tractocamión/pipa de Mefra Fletes;
- 28,262 litros de diésel;
- documentos que señalaban a Ecocarburante como destinataria;
- número de pedimento que habría sido presentado por otras pipas;
- documentos de importación vía Tuxpan que los inspectores consideraron incongruentes;
- determinación reportada de omisión del impuesto de importación.

Esta es una conexión mucho más fuerte que compartir un proveedor o agente aduanal genérico porque existe **una operación individualizada** con transportista, volumen, fecha y destinatario.

Aun así, la Ola 11 no dispone del acta primaria completa: la relación se apoya en la reproducción/reconstrucción documental de MCCI.

## 6. Ecocarburante ↔ IPS ↔ Mefra

MCCI revisó actas corporativas según las cuales **Impulsora de Productos Sustentables (IPS)** y Ecocarburante mantuvieron una relación financiera/corporativa: una deuda de IPS por 175 millones de pesos habría sido utilizada para capitalizar Ecocarburante en diciembre de 2020.

La misma investigación documenta personas compartidas entre Ecocarburante, IPS y Mefra.

### Miguel Castellanos Cruz

Bridge profesional:

- representante de Ecocarburante;
- representante de Mefra;
- vinculado societariamente a otras compañías del entorno.

Su centralidad profesional justifica investigación; **no prueba conocimiento de ilícitos**.

### José Isabel Murguía Santiago

MCCI documenta:

- accionista/administrador de Mefra desde 2019;
- socio de IPS desde 2020.

Eso crea una arista societaria entre la isla transporte y la isla importación/comercialización.

## 7. Galem Energy ↔ IPS

Forbes documentó en 2021 que **Galem Energy había sido propietaria/accionista de IPS** y que sus dueños transfirieron las acciones en septiembre de 2020.

SENER confirma independientemente que IPS recibió en mayo de 2019 el permiso de importación de diésel `1701C119000173` por hasta **1,000 millones de litros**.

Por tanto aparece un corredor histórico legítimo y verificable:

`Galem -B→ IPS -B→ Ecocarburante`

mientras la causa reportada añade:

`Galem -C→ Ecocarburante/Gutasa`.

Las dos rutas se sostienen con fuentes distintas, lo que aumenta el interés investigativo, no la culpabilidad.

## 8. Eric Daniel Zamora Delgadillo / Agrícola Boreal

MCCI documenta a **Eric Daniel Zamora Delgadillo** como accionista de Ecocarburante y apoderado de IPS, y reporta un vínculo corporativo histórico con **Agrícola Boreal**.

Treasury/OFAC sancionó a Agrícola Boreal el 4 de abril de 2016 dentro de una acción dirigida contra la red empresarial de **Los Cuinis**.

Regla aplicada:

> **sanción a empresa ≠ sanción personal automática a todos sus exsocios, presidentes, empleados o representantes.**

Por ello la arista Zamora→Agrícola se separa de Agrícola→OFAC.

## 9. H17 — Maquiladora como puente multi-isla

**Se fortalece como puente topológico**, pero la pieza que importa sigue faltando.

Subiría si aparecen:

- factura Maquiladora↔empresa de la red;
- pedimento;
- monto/volumen;
- carta porte;
- pagos;
- declaración que pruebe conocimiento del origen/documentación irregular.

Bajaría si la causa muestra que Maquiladora fue una contraparte periférica que adquirió combustible de buena fe y no tenía forma razonable de conocer irregularidades upstream.

## 10. H20 — Columna vertebral comercial multi-isla de la causa 325/2025

Nueva hipótesis.

La causa parece reunir:

- Marina / Farías;
- importadores/comercializadores;
- empresas con contratos públicos;
- transportistas;
- puertos;
- redes corporativas Jalisco/Nuevo León;
- eventos de inspección y decomisos.

Pero todavía existe una explicación rival sencilla: **una macrocausa puede reunir contrapartes comerciales de tipos muy distintos sin que exista una sola estructura de mando**.

La prueba exige extraer los 20 tomos y construir una matriz por hecho, no por nombre.

## 11. H21 — Contaminación retrospectiva

Nueva regla de red-team.

Un contrato público de 2019/2020 no puede reclasificarse automáticamente como ilícito porque años después alguno de sus participantes aparezca en una investigación.

Secuencia correcta:

```text
contrato público
→ suministro concreto
→ lote/documento/pedimento
→ irregularidad demostrada
→ conocimiento o participación
```

No:

```text
empresa investigada años después
→ todo contrato histórico era ilícito
```

## 12. Resultado sobre Andy / López Beltrán

**H01 no avanza.**

Ola 11 no encuentra:

- participación de Andy en Maquiladora;
- vínculo con Galem/Gutasa/Ecocarburante/Mefra/IPS;
- decisión sobre contratos AIFA;
- dinero;
- firma;
- instrucción;
- comunicación;
- conocimiento operacional.

El nuevo corredor emerge independientemente del círculo López Beltrán–Olán, lo que sigue favoreciendo la exploración de explicaciones sistémicas/multired frente a una teoría centrada forzosamente en una sola familia.

## Fuentes principales

- El Universal, 14 sep 2025 — causa 325/2025 y empresas.
- La Jornada, 23 ene 2026 — orden judicial de acceso a 20 tomos.
- ASF, Cuenta Pública 2019 — adquisiciones de diésel para AIFA.
- CRE — permisos de comercialización.
- SENER — permisos de importación Gutasa/IPS.
- MCCI, 30 jun 2025 — documentos corporativos, contratos e inspección Matamoros 2020.
- N+ — investigación de Mefra Fletes tras decomisos 2025.
- Forbes México — evolución accionaria Galem/IPS.
- U.S. Treasury/OFAC — Agrícola Boreal, 2016.
- CNH/Rondas México — existencia/participación sectorial de Galem Energy.

## Siguiente target

La siguiente ola debería ser **Ola 12 — Extract the 20 Tomes / Company Matrix**.

Prioridad:

1. localizar amparos, sentencias, versiones públicas y anexos que reproduzcan fragmentos de la causa 325/2025;
2. identificar todos los nombres empresariales y clasificarlos por **rol procesal**, no sólo por presencia;
3. extraer específicamente el proveedor de Maquiladora;
4. cruzar operadores repetidos —personas, domicilios, notarios, representantes, transportistas—;
5. separar `empresa investigada`, `contraparte`, `cliente`, `proveedor`, `transportista`, `permisionario` y `empresa mencionada`.

La Ola 11 demuestra que **la granularidad del rol dentro del expediente importa más que simplemente aparecer en él**.
