# Ola 10 — Identify the Three / Petrofactureros Multi-Island Bridge

**Corte:** 19 de agosto de 2026

## Pregunta

La FGR informó el 29 de mayo de 2026 que durante cuatro cateos de FEMDO en Nuevo León se aseguró documentación probablemente relacionada con **al menos tres empresas investigadas por delitos en materia de hidrocarburos y operaciones con recursos de procedencia ilícita**. La autoridad no publicó sus nombres.

La misión de esta ola fue intentar identificar esas tres empresas sin inferirlas por proximidad narrativa.

## Resultado ejecutivo

**No fue posible identificar responsablemente el trío.** La identidad de las tres empresas sigue siendo un target documental y no debe rellenarse con candidatos por intuición.

Sin embargo, la investigación produjo un puente multi-isla más fuerte y reproducible: **Maquiladora de Lubricantes, S.A. de C.V.**

La empresa aparece en cuatro contextos independientes:

1. **Operativo Petrofactureros 2026.** Jesús Ricardo Puente Díaz, documentado oficialmente como representante legal de Maquiladora, fue identificado por medios convergentes como la persona detenida durante los cateos FEMDO de mayo. Un punto de acuerdo del Congreso de Nuevo León menciona expresamente a Maquiladora y a su administrador único detenido en la operación.
2. **Puerto Dos Bocas / Tabasco.** Directorios oficiales registran a Maquiladora como prestador de recolección, acopio y transporte de residuos peligrosos, aceites y aguas oleosas, con Puente Díaz como representante.
3. **Frontera / SEMAR.** UNICAPAM mantiene autorizaciones para servicios de desechos portuarios en Frontera, Tabasco.
4. **Causa penal 325/2025.** El Universal reportó que Maquiladora aparece dentro de esa macrocausa por compras de combustible a una red señalada de utilizar documentación falsa. La misma causa es la que mantiene bajo proceso a Manuel Roberto Farías Laguna por acusaciones relacionadas con hidrocarburos, delincuencia organizada y lavado.

Este puente existe sin pasar por Andy, Amílcar Olán o Portacelis.

## Corrección de Ola 9

Ola 9 describió “Los Petrofactureros” como una denominación principalmente periodística porque el comunicado FGR del 29 de mayo no utilizaba públicamente el nombre.

Ola 10 localizó una fuente oficial anterior que corrige esa lectura: el **Gabinete de Seguridad del 22 de abril de 2026** sí utilizó expresamente el nombre **Los Petrofactureros** y describió una red de personas físicas y morales vinculadas a más de 40 empresas utilizadas presuntamente para simular actividades logísticas, energéticas y de transporte sin infraestructura real.

El nodo fue actualizado en lugar de duplicarse.

## Cronología mínima

### 2017

CRE otorgó a Maquiladora de Lubricantes el permiso de comercialización de petrolíferos **H/20572/COM/2017**.

### 2018–2024

Directorios oficiales de Puerto Dos Bocas muestran a la empresa como prestador de servicios vinculados con residuos peligrosos y aceites. Jesús Ricardo Puente Díaz figura como representante legal.

La presencia de la empresa en el puerto es una actividad regulada y **no demuestra participación en la Refinería Dos Bocas**. Por esta razón el grafo separa `puerto_dos_bocas` de `dosbocas` (refinería/proyecto).

### 2024–2029

SEMAR/UNICAPAM registra a Maquiladora en Frontera, Tabasco, con autorizaciones para servicios de desechos MARPOL.

### 2025

El Universal, al reconstruir la causa penal 325/2025, reportó que Maquiladora de Lubricantes aparece por compras a una red de empresas señaladas de utilizar documentación falsa para ingresar hidrocarburos a México.

El vínculo se clasifica **C — reportado** hasta incorporar la pieza judicial primaria que individualice la afirmación.

También existen rastros administrativos/fiscales independientes: Gobierno de Nuevo León publicó notificaciones de comercio exterior a la empresa y el TFJA registra un litigio de Maquiladora frente a una autoridad fiscal/SAT. Estos hechos prueban controversias regulatorias, no delitos.

### 22 abril 2026

El Gabinete de Seguridad presentó oficialmente la red **Los Petrofactureros**. Informó que el análisis fiscal y financiero detectó personas físicas y morales vinculadas a más de 40 empresas. La autoridad identificó a “Héctor Iván N” como coordinador de logística para obtención, carga, trasvase, distribución y comercialización de gasolina y diésel en varios estados.

Fuentes judiciales posteriores identificaron al procesado como **Héctor Iván Pineda Torres**. Vinculación a proceso no equivale a sentencia.

### 28–29 mayo 2026

FEMDO cateó inmuebles en San Pedro Garza García, Monterrey, Escobedo y Salinas Victoria. FGR informó la detención de “Jesús N” y documentación relacionada con **al menos tres empresas** investigadas por hidrocarburos y lavado.

El Universal, La Jornada y otros medios identificaron al detenido como **Jesús Ricardo Puente**.

### 10 junio 2026

El Congreso de Nuevo León registró un punto de acuerdo que menciona expresamente a **Maquiladora de Lubricantes**, cuyo administrador único había sido detenido en la operación contra Los Petrofactureros.

## ¿Es Maquiladora una de “las tres”? 

**No se puede afirmar.**

Es un candidato razonable porque:

- Puente era su representante/administrador documentado;
- Puente fue detenido durante los cateos;
- la empresa ya aparece reportada en otra investigación federal de hidrocarburos;
- Código Magenta también afirma que aparece en el supuesto oficio FEMDO de 353 entidades.

Pero la documentación incautada pudo pertenecer a otras empresas, a clientes, proveedores o terceros. FGR no publicó el inventario ni los nombres.

Por ello el grafo usa una arista **E — hipótesis** entre Maquiladora y `three_companies_target`.

## Puente hacia la causa 325/2025

La aparición reportada de Maquiladora en la causa 325/2025 resulta especialmente relevante porque esa causa también incluye a **Manuel Roberto Farías Laguna**.

La topología queda:

```text
Los Petrofactureros
        |
        C
        |
Maquiladora de Lubricantes
   |         |           |
   A         A           C
   |         |           |
Puerto     Frontera   Causa 325/2025
Dos Bocas     |           |
              |           B
              |           |
            SEMAR   Manuel R. Farías
                          |
                       huachicol
```

Esto **no demuestra que Petrofactureros y la red naval sean una sola organización**. Sí demuestra que una misma compañía aparece en contextos que antes eran islas separadas del grafo.

## Conexión política cross-party

Grupo Reforma reportó que Maquiladora pagó aproximadamente **15.06 millones de pesos** a **GMA Firma Jurídica Fiscal** en ocho facturas por honorarios entre noviembre de 2021 y marzo de 2022, y dijo haber verificado las facturas ante SAT.

El despacho es atribuido a **Samuel Orlando García Mascorro**, padre del gobernador de Nuevo León **Samuel Alejandro García Sepúlveda**.

El grafo deliberadamente **no crea una arista Samuel García → Maquiladora**.

La ruta es:

```text
Maquiladora -C→ GMA -C→ Samuel Orlando García Mascorro -B→ Samuel García
```

Su punto más débil es C y la semántica es **prestación profesional / parentesco**, no participación criminal.

Esta cadena se incorpora como control cross-party y como posible target documental para saber qué servicios se prestaron. No es prueba de conocimiento por parte del gobernador, su padre o el despacho.

## H15 — FEMDO 353

H15 se fortalece moderadamente, pero el supuesto oficio sigue sin autenticarse.

Código Magenta había nombrado a Maquiladora dentro del universo de 353. Ahora Maquiladora emerge independientemente en una operación FEMDO posterior y en la causa 325/2025. Esto hace el lead más interesante, pero no prueba que el documento de 353 sea auténtico.

## H17 — Maquiladora como puente multi-isla

**Estado:** fuerte como puente factual; significado criminal indeterminado.

La existencia del puente es objetiva a nivel corporativo/regulatorio. Su interpretación requiere separar:

- actividad portuaria legítima;
- actividad comercial de petrolíferos;
- acusaciones/investigaciones;
- actuaciones de personas físicas;
- posibles relaciones financieras.

## H18 — Identidad de las tres empresas

**Estado:** abierta.

La regla de esta ola es explícita:

> **una empresa plausible no se convierte en una de “las tres” hasta que una orden de cateo, inventario, imputación o expediente la nombre.**

## H19 — Cross-party professional adjacency

La relación Maquiladora → despacho del padre de Samuel García sirve como un test de nuestro sesgo político. Si el proyecto sólo considerara relaciones profesionales sospechosas cuando apuntan hacia Morena/AMLO, produciría una narrativa sesgada.

La explicación nula aquí es fuerte: un despacho fiscal puede prestar servicios ordinarios a un cliente energético sin conocer conductas ilícitas del cliente.

## Resultado respecto a H01 Andy↔huachicol

**Sin avance material.**

La Ola 10 descubre un puente relevante que no necesita pasar por Andy. No aparece evidencia de que Andy haya seleccionado, financiado, instruido, contratado o tenido conocimiento de Maquiladora de Lubricantes, Jesús Ricardo Puente, Los Petrofactureros o la causa 325/2025.

Esto favorece metodológicamente la pregunta maestra del proyecto: el grafo debe permitir que la estructura emerja sin obligar a que AMLO o su familia sean el centro.

## Targets para la siguiente investigación

Prioridad documental:

1. **Inventario de los cateos FEMDO del 28–29 mayo 2026** y nombres de las tres empresas.
2. **Imputación / causa de Jesús Ricardo Puente**, incluyendo persona moral, domicilios y bienes asegurados.
3. **Pieza judicial de la causa 325/2025** donde aparezca Maquiladora y el proveedor/red a la que habría comprado combustible.
4. **Contrato y conceptos de servicios Maquiladora ↔ GMA**, para establecer si fueron defensa fiscal ordinaria, litigio regulatorio u otro servicio.
5. **Clientes/proveedores de Maquiladora 2019–2025**, separando operaciones legítimas de las que estén individualizadas en investigaciones.
6. **Rastreo del permiso H/20572/COM/2017**, modificaciones, volúmenes y reportes regulatorios.

## Regla que deja Ola 10

> **Una empresa puede ser un puente real entre islas sin que eso convierta a las islas en una sola organización.**

La existencia del puente y el significado del puente son dos preguntas distintas.
