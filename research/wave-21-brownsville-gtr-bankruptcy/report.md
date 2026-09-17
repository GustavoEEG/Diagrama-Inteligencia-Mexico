# Ola 21 — Brownsville GTR Chapter 7 / Creditor–Equity–Asset Graph

**Corte:** 17 de septiembre de 2026  
**Pregunta:** ¿qué puede reconstruirse del Chapter 7 de Brownsville GTR LLC y qué relaciones de propiedad, acreedores, activos o insiders pueden cruzarse de forma documentada con Ballast, Portacelis y el resto del grafo?

## Conclusión ejecutiva

La Ola 21 confirma que el expediente 4:26-bk-35479 del U.S. Bankruptcy Court for the Southern District of Texas contiene exactamente los documentos de disclosure que buscábamos —Schedule A/B, Statement of Financial Affairs, Amendment to List of Creditors y Equity Security Holders—, pero **el contenido de esos documentos no quedó accesible/reproducible mediante las fuentes abiertas consultadas en esta ola**. Por tanto, el proyecto no inventa nombres de acreedores, equity holders, activos o transferencias.

El docket sí permite registrar hechos primarios/procesales importantes: Brownsville GTR presentó Chapter 7 voluntario el 30 jul 2026; el caso está marcado como **No Asset**; el aviso a acreedores del 27 ago reporta **100 notices**; la reunión 341 está programada para el 22 sep 2026; y el trustee es Christopher R. Murray. El rango patrimonial publicado por Houston Business Journal con base en registros judiciales es de **US$1–10M en activos** y **US$10–50M en pasivos**. "No asset" no significa literalmente cero activos; describe el estado procesal de distribución del Chapter 7 y no debe mezclarse con los rangos declarados.

La ola también mejora la capa corporativa previa: registros derivados de Texas Secretary of State muestran a **AWJR LLC** y **Ballast Partners LLC** como compañías listadas como officers de Brownsville GTR en distintos momentos, y ubican a Aaron C. Webster como manager de AWJR y Ballast. Esto no demuestra que AWJR o Ballast sean equity holders actuales del deudor en 2026; para eso precisamente necesitamos el docket #10.

El hallazgo metodológico principal es que el expediente de bancarrota **no resolvió todavía** la estructura económica de Brownsville GTR, pero convierte esa estructura en un target documental concreto y fechado. La siguiente ola debe concentrarse en obtener el contenido de los filings #5, #7, #9 y #10, o una copia RECAP/PACER/legal-data equivalente, y cruzar cada nombre con el grafo.

---

## 1. Hechos procesales confirmados

El docket público del caso registra:

- caso: `4:26-bk-35479`;
- tribunal: U.S. Bankruptcy Court, Southern District of Texas, Houston;
- capítulo: 7;
- presentación voluntaria: 30 jul 2026;
- juez: Alfredo R. Perez;
- trustee: Christopher R. Murray;
- estado listado: `No Asset`;
- reunión 341: 22 sep 2026;
- docket #5: Schedule A/B;
- #7: Statement of Financial Affairs for Non-Individual;
- #9: Amendment to List of Creditors;
- #10: Equity Security Holders;
- certificado de envío de la reunión de acreedores: 100 notices.

La existencia de esos filings es A/procesal. Su contenido material sigue **no recuperado** en esta ola.

## 2. Qué significa y qué no significa `No Asset`

El docket marca el caso como `No Asset`. En un Chapter 7 empresarial esto normalmente significa que, al estado actual del caso, el trustee no prevé una distribución a acreedores no garantizados. No equivale a decir que el deudor declaró literalmente cero activos.

Houston Business Journal publicó, a partir de registros de bancarrota, rangos declarados de:

- activos: US$1,000,001–10,000,000;
- pasivos: US$10,000,001–50,000,000.

La combinación `No Asset` + rango positivo de activos no es contradictoria: el valor realizable, gravámenes, prioridades y costos pueden dejar sin distribución a acreedores generales.

## 3. El dato de los 100 avisos

El BNC Certificate of Mailing de la reunión 341 reporta **100 notices**. Esto indica un universo de notificación amplio, pero **no equivale automáticamente a 100 acreedores únicos**: pueden existir duplicados, partes interesadas, agencias, abogados u otros destinatarios.

Por eso la regla es:

`100 notices ≠ 100 acreedores únicos`.

La creditor matrix sigue siendo necesaria.

## 4. AWJR LLC entra al grafo

CorporationWiki, basado en registros de Texas Secretary of State, muestra que Brownsville GTR ha listado como officers a:

- AWJR LLC — activo;
- Ballast Partners LLC — histórico/inactivo en ese rol.

El mismo corpus corporativo asocia a Aaron C. Webster con AWJR LLC y Ballast Partners como manager.

Esto añade una pieza nueva:

`Aaron Webster → AWJR`  
`Aaron Webster → Ballast`  
`AWJR / Ballast → Brownsville GTR (roles corporativos históricos)`

Pero no autoriza a afirmar:

- que AWJR sea accionista actual de Brownsville GTR;
- que Ballast sea equity holder en 2026;
- que exista transferencia patrimonial impropia entre ellas;
- que los roles corporativos expliquen las operaciones Portacelis.

El filing #10 es el documento que puede resolver la parte de equity.

## 5. Aaron Webster y red corporativa

Registros derivados de Texas SOS muestran a Aaron C. Webster asociado a múltiples compañías, entre ellas AWJR LLC, Ballast Partners LLC y A&K Fuels LLC. La existencia de una red corporativa personal no es anomalía por sí misma; empresarios del sector suelen operar varias sociedades.

El valor de esta red es estrictamente de búsqueda: si alguno de esos nombres reaparece en los schedules de Brownsville GTR como insider, acreedor, deudor, lease counterparty o equity holder, la conexión podrá elevarse.

## 6. Lo que NO logramos recuperar

No se obtuvo en esta ola el texto reproducible de:

- Schedule A/B;
- Statement of Financial Affairs;
- creditor matrix completa/amendada;
- Equity Security Holders;
- contratos de lease;
- cuentas por cobrar a Portacelis u otros clientes mexicanos;
- pagos/transferencias a Ballast, AWJR o insiders;
- números de railcar dentro de los assets.

La ausencia de esos datos en web abierta **no significa que no estén en PACER**.

## 7. H38 — Ballast como intermediario cross-client

**Cambio:** permanece investigable, sin elevación.

A favor:

- Ballast aparece en la estructura corporativa histórica de Brownsville GTR;
- N+ reporta a Ballast como arrendador de equipo a Ingemar;
- Brownsville GTR fue proveedor ferroviario principal de Portacelis.

En contra:

- Ola 20 no encontró un mismo carro físico identificable entre la muestra Ingemar y Ballast/BACX;
- esta ola no recuperó leases ni cuentas de Brownsville GTR;
- misma red corporativa ≠ misma transacción.

## 8. H39 — la bancarrota puede revelar la estructura económica real de Brownsville GTR

**Nueva / investigable.**

Predicción si es útil:

los filings #5/#7/#9/#10 deberían revelar una o más de estas categorías:

- equity holders;
- insiders;
- cuentas por cobrar/pagar;
- leases y equipo;
- transferencias pre-petition;
- acreedores comerciales;
- relaciones con Ballast/AWJR;
- clientes o contrapartes mexicanas.

Falsador:

si los documentos contienen sólo obligaciones genéricas sin cruces con nuestro universo, el valor de la rama Brownsville GTR disminuirá y habrá que regresar al anexo SAT/railcar roster.

## 9. Implicación para captura funcional

Esta ola no eleva H36. Una bancarrota privada puede revelar flujos y contrapartes, pero no demuestra colaboración estatal. Incluso si aparecieran Portacelis, Ballast o Ingemar en el expediente, eso demostraría relación económica, no captura de una función pública.

## 10. Próxima dirección

**Ola 22 — Recover the Bankruptcy Filings / Insider–Creditor Matrix**

Objetivo:

1. recuperar filings #5, #7, #9 y #10 mediante PACER/RECAP/otra fuente reproducible;
2. extraer equity holders, insiders, acreedores, deudores y leases;
3. cruzar nombres contra Ballast, AWJR, Portacelis, Ingemar, L Energy, MG Energy, Ikon y el resto del grafo;
4. revisar transferencias de los 90 días previos al 30 jul 2026 y, para insiders, el periodo relevante más amplio sin asumir que cualquier transferencia sea recuperable;
5. mantener como vía secundaria el full roster de railcars Portacelis/Ingemar.

Hasta obtener esos documentos, agregar supuestos acreedores o accionistas sería especulación y no debe entrar al grafo factual.