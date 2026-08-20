# Ola 6 — Reverse Graph / Bridge Hunt

**Corte:** 19 de agosto de 2026  
**Pregunta:** si dejamos de escoger el siguiente blanco por narrativa y usamos la topología del universo, ¿qué puente inesperado merece investigación independiente?

## Resumen ejecutivo

Ola 6 introduce análisis de grafo reproducible para evitar que la investigación dependa únicamente de intuición. Se calculó degree, betweenness, articulation points, bridges y shortest paths sobre dos universos: A–C y A–G.

El análisis A–C confirmó que Portacelis Gas & Oil es el nodo de mayor intermediación del universo actual, pero también reveló un problema: esa centralidad está parcialmente causada por el hecho de que las Olas 2–5 expandieron deliberadamente su vecindario. Para reducir el sesgo de construcción, no se eligió Portacelis de nuevo como blanco.

El puente transversal seleccionado fue **Juan Hermilo Chávez Rodríguez / patente aduanal 3677**, porque conecta operaciones separadas de Portacelis e Ingemar en Nuevo Laredo y, durante la verificación, apareció un dato material nuevo: Chávez fue detenido y vinculado a proceso en julio de 2026 dentro de la causa federal asociada a la presunta red ferroviaria de Ingemar. La Jornada reportó después que, por edad y salud, podrá continuar el proceso desde su domicilio.

Este hallazgo **no convierte en ilícita ninguna operación de Portacelis tramitada por la patente 3677**. El mismo agente aparece en muestras de importaciones no energéticas, lo que demuestra que funciona como hub profesional multisectorial. Esa evidencia fortalece simultáneamente la razón para investigar al puente y la obligación de no sobreinterpretarlo.

## 1. Qué dijo el propio grafo

Antes de añadir los nuevos hallazgos, el universo tenía 75 nodos y 108 aristas.

En el núcleo A–C, Portacelis registró degree 21 y betweenness normalizada aproximada de 0.663. Le siguieron Juan Carlos de la Cruz Murillo (~0.360), Amílcar Olán (~0.281) y el concepto HUACHICOL FISCAL (~0.255).

Las métricas completas están en `metrics.md`.

### Problema metodológico: centralidad endógena

No debe confundirse:

`nodo muy investigado → muchas aristas`

con:

`nodo objetivamente central en el fenómeno real`.

El primer proceso puede producir artificialmente el segundo dentro de nuestra base.

Por eso la selección de Ola 6 exigió un puente que conectara islas distintas y que no hubiera sido creado como protagonista por las olas recientes.

## 2. El puente seleccionado: patente 3677

ANAM identifica a **Juan Hermilo Chávez Rodríguez** como agente aduanal activo en Nuevo Laredo con patente nacional **3677**.

Una muestra Panjiva de Brownsville GTR→Portacelis registra:

- entrada: Nuevo Laredo;
- transporte: ferrocarril;
- agente aduanal: 3677;
- permiso de Portacelis: `1701C124002733`.

Una muestra separada de Ingemar/Belar Fuels registra:

- entrada: Nuevo Laredo;
- transporte: ferrocarril;
- agente aduanal: 3677;
- permiso distinto de Ingemar: `1701C123000151`.

La inferencia factual es limitada:

`Portacelis → patente 3677 ← Ingemar`.

Eso demuestra uso de un mismo prestador/patente en operaciones separadas. No demuestra que las empresas se conocieran, coordinaran o compartieran un propósito ilícito.

## 3. El cambio de importancia: Chávez está procesado en la causa Ingemar

FGR informó en el Comunicado 466/26 del 23 de julio de 2026 que obtuvo vinculación a proceso contra ocho personas posiblemente relacionadas con una red de contrabando de combustible. El comunicado identifica por nombre abreviado a `Juan N` y `Luis N` y señala que fueron vinculados por probable delincuencia organizada y contrabando.

La Jornada identifica a `Juan N` como **Juan Hermilo Chávez Rodríguez**, agente aduanero, y reporta que fue detenido el 16 de julio. El 12 de agosto informó que un tribunal autorizó que continuara el proceso en prisión domiciliaria por su edad y condiciones de salud.

Por tanto, el grafo puede afirmar con grado B:

`Juan Hermilo Chávez → vinculado a proceso en causa ferroviaria 2026`.

No puede afirmar:

- que sea culpable;
- que cualquier despacho suyo sea ilícito;
- que Portacelis supiera de la conducta investigada;
- que la operación Brownsville→Portacelis de 2025 forme parte de la causa Ingemar;
- que Portacelis e Ingemar integren una sola red criminal.

La vinculación a proceso es una resolución procesal y toda persona imputada conserva presunción de inocencia.

## 4. Luis Antonio Barrientos Juárez

Fuentes que citan documentación de la causa identifican a **Luis Antonio Barrientos Juárez** como dependiente autorizado de Juan Hermilo Chávez Rodríguez. FGR reportó que `Luis N` fue vinculado a proceso junto con `Juan N`; medios que cubren el expediente lo identifican como Barrientos.

El grafo incorpora dos relaciones diferentes:

- Barrientos → causa 2026: B, por la combinación de comunicado oficial e identificación periodística;
- Barrientos → Chávez como dependiente autorizado: C, porque todavía no incorporamos el registro administrativo primario que acredite directamente esa dependencia.

Esta separación evita que una atribución de expediente se convierta artificialmente en hecho primario.

## 5. Origen oficial: 33 ferrotanques en Ramos Arizpe

FGR Comunicado 482/26, de 27 de julio de 2026, señala que la investigación tuvo origen en **33 ferrotanques abandonados en Ramos Arizpe, Coahuila**. Tras inspecciones, muestras y peritajes, la pesquisa se amplió al análisis de la cadena logística completa.

Este punto entra como A porque es una descripción directa de la autoridad sobre el origen de su investigación.

No implica que todo actor de una cadena logística ferroviaria o aduanal esté relacionado con esa causa.

## 6. Red team: 3677 no es una patente exclusivamente energética

Éste es uno de los hallazgos más importantes de la ola.

Muestras Panjiva muestran la patente 3677 en operaciones ajenas a combustibles, entre ellas:

- productos para interiores de aeronaves;
- maquinaria industrial;
- herramientas/equipos industriales.

Por tanto, la misma evidencia que convierte a Chávez en un puente de investigación también destruye una interpretación demasiado fácil:

> “Si dos empresas usaron 3677, pertenecen a la misma red.”

No. La patente atiende múltiples sectores.

La pregunta correcta pasa a ser cuantitativa:

> **¿Los importadores de combustible posteriormente investigados están sobrerrepresentados entre los clientes de 3677 respecto de la cuota normal de mercado del agente?**

Sin ese denominador no podemos distinguir señal de ruido.

## 7. H09 se fortalece, no se debilita

### H09 — Concentración comercial como explicación alternativa

La existencia de clientes no energéticos demuestra que 3677 funciona como un hub profesional general. Eso hace más plausible que Portacelis e Ingemar coincidieran simplemente porque ambos importaban por un corredor donde determinados agentes tienen presencia relevante.

Para falsar H09 necesitamos medir:

- total de operaciones de 3677;
- clientes únicos;
- distribución por sector/HS code;
- participación en Nuevo Laredo;
- proporción de hidrocarburos;
- proporción de clientes posteriormente investigados;
- comparación con patentes pares de similar tamaño.

## 8. Nueva H12 — Hub aduanal compartido entre corredores de combustible

H12 no dice que exista una conspiración común.

Pregunta si algunos agentes/dependientes funcionan como hubs recurrentes entre corredores de combustible que terminan apareciendo en investigaciones separadas.

### Evidencia que la favorece actualmente

- Portacelis usa 3677 en una operación documentada.
- Ingemar usa 3677 en una operación documentada.
- Juan Hermilo Chávez es titular activo de 3677 según ANAM.
- Chávez fue vinculado a proceso en la causa ferroviaria relacionada con Ingemar.
- Barrientos, reportado como su dependiente autorizado, fue procesado en la misma causa.

### Evidencia en contra / explicación ordinaria

- 3677 tramita mercancías no energéticas y diversos clientes.
- un agente importante puede atender competidores y empresas sin relación alguna;
- no hay evidencia pública incorporada de comunicación Portacelis↔Ingemar;
- no hay evidencia de que la operación de Portacelis con 3677 sea parte del expediente penal;
- no hay evidencia de beneficio financiero común entre ambos importadores.

### Qué aumentaría H12

- una concentración estadísticamente extraordinaria de importadores investigados entre clientes del agente;
- el mismo dependiente/mandatario firmando operaciones relevantes en varios casos;
- comunicaciones o instrucciones comunes;
- facturación/pagos conectados;
- pedimentos con patrones de discrepancia equivalentes y atribuibles a los mismos operadores;
- coincidencia temporal y logística más fuerte que la tasa base del corredor.

### Qué la debilitaría

- demostrar que 3677 concentra una cuota tan grande de Nuevo Laredo que el solapamiento es esperable;
- que las operaciones de Portacelis hayan sido revisadas y resulten documentalmente regulares;
- que diferentes equipos/dependientes procesaran a cada cliente sin interacción;
- ausencia de cualquier vínculo financiero/comunicacional tras revisar expedientes.

## 9. Una advertencia importante sobre shortest paths

El analizador encontró en A–C una ruta corta:

`Andy → AMLO → Ojeda → Marina → huachicol`.

Eso no es evidencia contra Andy. Es una secuencia de parentesco + jerarquía institucional + investigaciones sobre algunos miembros de una institución.

Cuando abrimos A–G, la arista F `Andy→huachicol` hace que la ruta más corta se vuelva directa.

La topología cambió; la evidencia no.

Por eso Ola 6 establece una regla nueva:

> **Nunca publicar una ruta de grafo sin mostrar el grado más débil de la ruta y la semántica de cada arista.**

## 10. H01 Andy↔huachicol

**Sin avance material.**

La investigación inversa no produjo evidencia de que Andy:

- conociera a Juan Hermilo Chávez;
- seleccionara la patente 3677;
- interviniera en operaciones Portacelis;
- tuviera contacto con Ingemar;
- recibiera dinero de ninguna de esas operaciones.

Las métricas que muestran a Andy como articulation point son un producto de relaciones familiares/políticas y de cómo se construyó el universo; no constituyen evidencia de conducta criminal.

## 11. Resultado de la ola

El siguiente puente no fue una celebridad política. Fue un **operador aduanal**.

Eso valida la idea original del proyecto: los puentes más informativos pueden ser contadores, agentes, dependientes, notarios, transportistas o identificadores administrativos.

Pero la misma ola demuestra el riesgo opuesto: los profesionales que atienden muchos clientes serán naturalmente centrales.

La tarea no es sólo encontrar hubs. Es demostrar cuándo un hub tiene una concentración **anormal** de eventos relevantes frente a su actividad ordinaria.

## 12. Próxima investigación recomendada

La siguiente ola debería construir el **baseline de aduanas y ferrocarril**, no perseguir todavía otra acusación:

1. medir el universo observable de la patente 3677;
2. comparar patentes 3677, 3830 y 3807;
3. identificar dependientes/mandatarios por operación cuando sea público;
4. contar importadores de combustibles vs otros sectores;
5. mapear ferrocarriles, terminales y arrendadores;
6. medir cuánto del aparente solapamiento desaparece al controlar por cuota de mercado;
7. sólo después buscar bridges estadísticamente anómalos.

Ésa sería una auténtica **Ola 7 — Baseline Aduanal / Network Control Group**.
