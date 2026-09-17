# Ola 17 — L. Energy Cross-Island Supplier Graph + News Delta

**Corte:** 16 de septiembre de 2026  
**Pregunta principal:** ¿la recurrencia de L. Energy International entre Carvel, Karina Guerrero e Ingemar constituye una coincidencia comercial excepcional o puede explicarse por un proveedor estadounidense de alta frecuencia en el mercado mexicano?  
**Pregunta adicional:** ¿qué noticias publicadas desde el cierre de la Ola 16 abren nuevas rutas materiales en el grafo?

## Conclusión ejecutiva

La Ola 17 produce dos resultados distintos.

Primero, **recalibra L. Energy**. Panjiva indexa **2,166 registros de embarques de L Energy International con destino México**. Esto cambia la interpretación de la Ola 16: L. Energy sigue siendo un gran nodo de navegación, pero compartirlo como proveedor deja de ser, por sí solo, una anomalía fuerte. Se añaden clientes de control —Trámites Logísticos Mundiales, Quemex Hidrocarburos, Energéticos Regionales y Tramitadora Aduanal de Reynosa— para hacer visible el denominador.

Segundo, aparece una rama mucho más concreta: **L.E. International Fuel Supply, S.A. de C.V.**. La entidad mexicana tiene RFC `LIF1707192M8`, identidad jurídica validada por LEI, huella en Sector 13 de SAT y al menos una relación shipper/consignee visible con L Energy International. Un reportaje de octubre de 2025 la vinculó con cinco ferrotanques asegurados que contenían 750 mil litros; Steven y Laura McNear ejercieron después derecho de réplica, afirmaron que ya no eran accionistas cuando se publicó la nota y negaron ilícitos e investigación. La relación accionaria, por tanto, se modela como **histórica**, no vigente.

El barrido de noticias del 20 de agosto al 16 de septiembre de 2026 abre además tres rutas que compiten por ser la siguiente ola:

1. **Portacelis → SAT → FGR:** N+ reporta que SAT pidió a FGR investigar un perjuicio fiscal estimado en 834 mdp.
2. **Pemex → Deer Park → Ingemar → Crismon:** una investigación publicada el 14 de septiembre, basada en la causa contra Ingemar, atribuye más de un millón de litros de gasolina a cargamentos originados en Deer Park. Pemex confirma de manera independiente que es propietario total de Deer Park desde 2022.
3. **Farías → nombramientos/aduanas:** FGR informó sobre documentación aduanal y expedientes de personal naval localizada en una bodega vinculada a Manuel Roberto Farías; la defensa disputa la procedencia/presentación de parte de esa evidencia.

Finalmente, el 16 de septiembre la Fiscal General declaró que **no existen órdenes de aprehensión contra Andrés Manuel López Beltrán ni Amílcar Olán**. Ese dato se incorpora como contraevidencia procesal y corrige rumores publicados días antes.

---

## 1. L. Energy no es un proveedor raro: es un nodo de alta frecuencia

Panjiva muestra para L Energy International:

- 2,166 registros de embarques;
- destino México: 100% en el perfil consultado;
- HS 27 como categoría principal;
- ejemplos por ferrocarril y autotransporte a distintos puntos fronterizos.

El grafo incorpora cuatro controles comerciales:

- **Trámites Logísticos Mundiales** — Matamoros, 2023;
- **Quemex Hidrocarburos** — Nuevo Laredo, 2021, ferrocarril;
- **Energéticos Regionales** — Matamoros, 2019;
- **Tramitadora Aduanal de Reynosa** — Reynosa, 2019.

Esto obliga a modificar H31:

> `Carvel → L Energy ← Karina` sigue siendo factual/documentable, pero **L Energy compartida ≠ anomalía sin tasa base**.

La siguiente prueba no es encontrar más clientes de L Energy indefinidamente. Es reconstruir:

- número de clientes únicos por año;
- volumen por cliente;
- terminales;
- patentes/agentes;
- carros tanque;
- rutas;
- producto;
- fechas;
- concentración comercial.

Sólo entonces puede medirse si Carvel/Karina/Ingemar tienen un solapamiento superior a lo esperable.

## 2. L.E. International Fuel Supply: la rama mexicana

Bloomberg LEI valida:

- razón social: **L.E. International Fuel Supply, S.A. de C.V.**;
- RFC: `LIF1707192M8`;
- creación: 19 jul 2017;
- entidad: activa;
- domicilio jurídico reportado en Ciudad de México.

SAT, en el padrón de importadores de sectores específicos con corte al 31 de octubre de 2025, lista a la empresa como activa en **Sector 13 — Hidrocarburos y combustibles**.

Panjiva muestra una operación en la que:

`L Energy International LLC → L.E. International Fuel Supply S.A. de C.V.`

Esto establece una relación comercial observable. No se presume propiedad corporativa actual a partir del nombre.

## 3. McNear: separar relación histórica de propiedad actual

Texas Railroad Commission registra a:

- **L Energy International LLC** — managing member de Buckhead Midstream;
- **Steve McNear** — managing member de Buckhead Midstream.

El Universal publicó en octubre de 2025 que Steven Mark McNear y Laura Jordan McNear eran accionistas de L.E. International Fuel Supply. Ambos respondieron por separado:

- Steven McNear afirmó que **ya no era accionista al momento de la publicación**;
- Laura McNear afirmó lo mismo;
- ambos negaron participación en ilícitos y conocimiento de investigación.

Sus réplicas, sin embargo, utilizan la formulación de que **habían sido accionistas**. Por tanto la arista correcta es:

`Steven/Laura McNear → L.E. International Fuel Supply = relación accionaria histórica reconocida`

No:

`Steven/Laura McNear = propietarios actuales`.

Falta RPC histórico y actual para fechar entrada/salida y porcentajes.

## 4. Decomiso de 2025: incorporar evento y contradicción

El Universal reportó el 2 de octubre de 2025 que cinco ferrotanques con aproximadamente 750 mil litros de combustible fueron asegurados en Matamoros/Nuevo Laredo y los vinculó con L.E. International Fuel Supply. La pieza atribuyó a autoridades una hipótesis de ingreso irregular.

El proyecto no transforma esa publicación en sentencia. La modelación es:

- decomiso/aseguramiento reportado: **C**;
- vínculo empresa↔ferrotanques: **C** hasta expediente primario;
- caracterización de delito: **C/alegada**;
- derechos de réplica de exaccionistas: contraevidencia obligatoria.

El target documental es el expediente del aseguramiento: pedimentos, números de carro, producto, importador, agente, permisos y resolución posterior.

## 5. H32 — proveedor de alta frecuencia como explicación rival

**Nueva / red-team fuerte.**

Predicción si H32 es correcta:

- L Energy aparecerá con decenas o cientos de clientes independientes;
- los clientes utilizarán múltiples agentes, permisos y cruces;
- la coincidencia Carvel/Karina/Ingemar no concentrará terminales o carros de manera excepcional.

H32 se debilita si aparece, por ejemplo:

- mismo lote o BOL;
- misma terminal + carro tanque + ventana temporal;
- misma patente muy por encima de tasa base;
- misma contraparte financiera;
- mismos documentos reutilizados;
- operaciones encadenadas entre los clientes.

## 6. H33 — corredor L Energy ↔ L.E. Fuel Supply

**Nueva / investigable; no hipótesis criminal.**

A favor:

- relación comercial visible en Panjiva;
- huella regulatoria SAT Sector 13;
- relación histórica reconocida por Steven/Laura McNear;
- Steve y L Energy aparecen juntos como managing members de Buckhead Midstream.

En contra:

- compartir personas históricas y comercio transfronterizo puede ser una estructura empresarial legítima;
- no tenemos ownership actual;
- no tenemos contrato primario L Energy↔L.E. Fuel Supply;
- el evento de 2025 no está adjudicado y fue controvertido.

El valor está en que ofrece claves concretas: RFC, domicilios, exaccionistas, registros de comercio y expediente de aseguramiento.

---

# News Delta — 20 ago → 16 sep 2026

## 7. Portacelis: salto de suspensión/reportajes a solicitud SAT→FGR

El 1 de septiembre N+ reportó que el SAT solicitó a la FGR investigar a **Portacelis Gas & Oil** por presunta defraudación fiscal relacionada con importaciones de combustible y estimó un perjuicio por **834 millones de pesos**.

La publicación identifica además a **Juan Carlos de la Cruz Murillo** entre las personas mencionadas en la solicitud.

Esto sí cambia el estado del grafo: antes teníamos suspensión del padrón, comercio exterior y reportajes. Ahora existe una **actuación fiscal-penal reportada** posterior.

No elevamos todavía a A porque la declaratoria/querella del SAT no está incorporada en el repositorio.

### Target de máximo valor

Obtener:

1. declaratoria de perjuicio/querella SAT;
2. anexos de pedimentos;
3. cálculo que sustenta 834 mdp;
4. periodo exacto;
5. volúmenes declarados vs determinados;
6. personas jurídicas/físicas formalmente incluidas;
7. número de carpeta FGR.

Esta ruta vuelve a **Portacelis** candidata principal para la Ola 18.

## 8. FGR obtiene documentos físicos de la rama Ingemar

El 26 de agosto la FGR informó oficialmente que cateó dos bodegas en Ciudad de México y aseguró:

- pedimentos de importación;
- actas de asamblea;
- contratos.

La FGR afirmó que el material abre nuevas líneas dentro de la investigación ferroviaria de contrabando.

La existencia del cateo/documentos es A como acto de autoridad. Lo que esos documentos demuestren sobre culpabilidad sigue pendiente.

Este hallazgo es especialmente importante para nosotros porque son exactamente las clases documentales que veníamos identificando desde olas anteriores como techo del OSINT.

## 9. Deer Park entra en la rama Ingemar

El 14 de septiembre El País publicó, con base en documentación de la causa contra Ingemar, una ruta que incluye cargamentos de gasolina procedentes de **Deer Park Refining L.P.** por más de un millón de litros.

Independientemente, Pemex confirma que:

- adquirió la participación restante de Deer Park en enero de 2022;
- es propietario total;
- Deer Park opera como subsidiaria de Pemex.

Por tanto:

`Pemex → Deer Park` = **A**

`Deer Park → Ingemar en los cargamentos investigados` = **C**, porque deriva de una causa/reportaje y no debe transformarse en imputación automática a la refinería o a Pemex.

La misma publicación agrega:

- **Crismon Hidrocarburos y Derivados**, descrita en la investigación como vehículo financiero/contraparte;
- **Internacional de Fundentes**, descrita como destinatario previsto de determinados cargamentos.

Este es probablemente el **nuevo puente cross-island más importante del news delta** porque conecta una infraestructura de Pemex en Estados Unidos con una rama ya presente en el grafo, pero su significado causal sigue abierto.

## 10. Farías: del contrabando a una posible capa de nombramientos

El 7 de septiembre FGR informó, según cobertura contemporánea, que en una bodega vinculada a Manuel Roberto Farías Laguna había:

- listas de aduanas marítimas;
- expedientes de personal naval y altos mandos;
- documentos clasificados de seguridad nacional;
- armas.

La fiscal también sostuvo que los Farías intervenían en designaciones, ascensos y movimientos de personal en aduanas/Marina.

La defensa respondió al día siguiente disputando la procedencia y presentación de parte de esa evidencia.

El proyecto conserva ambas posiciones.

Analíticamente, esto abre una isla nueva:

`persona → nombramiento → aduana → periodo → operación/decomiso`

Si se obtienen listas o nombramientos concretos, podríamos cruzarlos con puertos, pedimentos y decomisos existentes. Esa ruta puede ser más informativa que seguir sólo empresas.

## 11. Contraevidencia actual: Andy y Olán

Durante los días previos al 16 de septiembre circularon notas que afirmaban que existía una orden de aprehensión contra Amílcar Olán.

El 16 de septiembre la Fiscal General Ernestina Godoy declaró que:

- **no existe orden de aprehensión contra Amílcar Olán**;
- **no existe orden de aprehensión contra Andy López Beltrán**.

La versión más reciente y atribuida directamente a la Fiscal General debe prevalecer sobre rumores no corroborados para el estado actual del grafo.

H01 permanece **baja / no demostrada**.

---

# Direcciones que deja Ola 17

La ola no deja una sola ruta; deja tres que ya tienen documentos concretos como objetivo.

## Dirección 1 — Portacelis SAT/FGR

Mayor valor documental inmediato.

**Pregunta:** ¿podemos obtener la declaratoria SAT y reconstruir transacción por transacción la diferencia que produce los 834 mdp?

Ruta potencial:

`Portacelis → proveedor US → ferrotanque/pedimento → aduana → volumen declarado → volumen determinado SAT → impuesto → carpeta FGR`

## Dirección 2 — Deer Park / Ingemar / Crismon

Mayor valor cross-island.

**Pregunta:** ¿qué diez carros/cargamentos vincula la causa con Deer Park y cómo pasan por Ingemar, Crismon, agente 3677 y destinatarios?

Ruta potencial:

`Pemex → Deer Park → Ingemar → Crismon / Internacional de Fundentes → Juan Hermilo/patente 3677 → frontera`

## Dirección 3 — Farías / Personnel Appointment Graph

Mayor valor institucional.

**Pregunta:** ¿qué nombramientos y aduanas aparecen en los expedientes recuperados y qué eventos del grafo ocurren durante sus periodos?

Ruta potencial:

`Farías → nombramiento → mando aduanal → puerto/aduana → operación → empresa`

## Prioridad sugerida por valor de información

**Ola 18: Portacelis SAT/FGR — 834M Declaratoria & Pediment Reconstruction.**

Es el camino con mayor posibilidad de elevar aristas existentes de C/D hacia B/A mediante una pieza fiscal concreta y, simultáneamente, puede conectar la columna Portacelis con proveedores estadounidenses, ferrocarril, agentes aduanales y personas ya presentes.

En paralelo, Deer Park/Ingemar queda como segunda ruta inmediata; si aparecen documentos primarios antes de terminar la 18, debe convertirse en expansión lateral de la misma ola o en Ola 19.

## H01

Sin avance incriminatorio. La actualización más reciente es contraevidencia procesal: FGR niega órdenes de aprehensión contra Andy y Olán. Ninguna de las nuevas rutas L Energy, Portacelis, Deer Park/Ingemar o Farías aporta por ahora dinero, propiedad, firma, comunicación, instrucción o beneficio directo atribuible a Andy.
