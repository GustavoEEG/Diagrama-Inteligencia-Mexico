# Protocolo Maestro — Diagrama Inteligencia México

**Metodología, gobernanza y continuidad del Intelligence Link Analysis**  
**Versión 1.0 — 19 de agosto de 2026**

# 0. Propósito de este documento

Este documento es la **fuente metodológica maestra** del proyecto **Diagrama Inteligencia México**. Su función no es demostrar una teoría concreta ni resumir una sola investigación, sino establecer de manera explícita **qué estamos construyendo, para qué, con qué reglas, cómo se incorpora evidencia, cómo se separan hechos de hipótesis y cómo debe continuar el trabajo cuando una conversación de ChatGPT se agote o sea reemplazada por otra**.

El repositorio canónico del proyecto es:

**GustavoEEG/Diagrama-Inteligencia-Mexico**

La visualización pública del tablero es:

**https://gustavoeeg.github.io/Diagrama-Inteligencia-Mexico/**

El principio operativo es simple:

> **El repositorio es la memoria persistente del proyecto. Las conversaciones son sesiones de investigación temporales.**

Por ello, una conversación nueva debe leer primero este protocolo y después consultar el estado actual del repositorio antes de continuar cualquier ola de investigación.

## 0.1 Instrucciones obligatorias para una conversación nueva

Cuando se retome el proyecto en una conversación nueva, el asistente debe seguir este orden:

1. Leer este **Protocolo Maestro** completo.
2. Consultar el repositorio `GustavoEEG/Diagrama-Inteligencia-Mexico`, rama `main`.
3. Leer al menos `README.md`, `docs/methodology.md` o su sucesor, y los archivos vigentes de `data/`.
4. Revisar los PR abiertos y los últimos PR fusionados para conocer qué ola está en curso y qué cambió recientemente.
5. No asumir que los conteos de nodos, aristas, hipótesis o fuentes contenidos en este documento siguen siendo actuales; esos datos son dinámicos y la rama `main` es la fuente de verdad.
6. Identificar la pregunta de la siguiente ola y el conjunto de puentes críticos pendientes.
7. Para hechos públicos actuales, investigaciones, funcionarios, sanciones, causas judiciales, contratos, noticias o roles que puedan haber cambiado, realizar búsqueda web actualizada antes de afirmar nada.
8. Mantener siempre separadas las capas de **hecho, reporte, inferencia, hipótesis y especulación**.
9. No realizar cambios sustantivos directamente en `main`. Trabajar mediante rama temática y Pull Request, salvo una intervención técnica excepcional y explícitamente justificada.
10. Al cerrar una ola, actualizar el grafo, las fuentes, las hipótesis afectadas, las contradicciones y el listado de preguntas abiertas.

Si el usuario dice simplemente **“continuemos con el proyecto”**, estas instrucciones deben interpretarse como el protocolo de arranque por defecto.

# 1. Misión del proyecto

Construir un **universo de inteligencia de fuentes abiertas, versionado y auditable**, que represente actores, organizaciones, empresas, instituciones, proyectos, eventos, activos, operaciones y relaciones relevantes para entender redes de poder, contratación, corrupción, crimen organizado, contrabando de combustibles, megaproyectos, financiamiento político, captura institucional, aplicación de la ley y presión internacional en México, con énfasis temporal inicial en **2018–2026**.

El proyecto nació de una investigación sobre **AMLO y sus hijos**, pero metodológicamente dejó de ser un grafo centrado en una familia. La pregunta rectora evolucionó hacia una formulación más robusta:

> **¿Qué estructura —o combinación de estructuras— explica mejor el conjunto de anomalías observadas en México entre 2018 y 2026?**

El grafo no debe colocar a AMLO, a sus hijos, a Morena, a un cartel ni a ninguna otra entidad en el centro por decisión previa. **La centralidad debe emerger de los datos.**

# 2. Qué NO es este proyecto

Este proyecto no es:

- una acusación penal;
- una lista de culpables;
- un repositorio de rumores presentado como hechos;
- una herramienta para inferir culpabilidad por proximidad social;
- un tablero partidista diseñado para confirmar una conclusión predeterminada;
- una colección indiscriminada de nombres privados o datos personales;
- una “teoría de todo” que obligue a conectar eventos independientes;
- una sustitución de una investigación judicial, periodística o forense.

La existencia de una ruta `A → B → C → D` no implica que A conozca a D, que A controle a D, que exista coordinación entre ambos, ni que A sea responsable de la conducta de D.

**La proximidad en un grafo es una pista de investigación, no una conclusión de responsabilidad.**

# 3. Arquitectura conceptual: un solo universo, no siete mapas separados

Originalmente se plantearon “niveles” separados: hechos, periodismo, alegaciones, red de vínculos, hipótesis, falsificación y conspiración. La arquitectura definitiva los absorbe en **un único universo de inteligencia**.

Ese universo contiene simultáneamente:

**núcleo documental → relaciones fuertemente documentadas → reportes y alegaciones → inferencias → hipótesis investigables → hipótesis conspirativas → wildcards**

La diferencia no está en qué mapa aparece una relación, sino en **cómo está etiquetada epistemológicamente**.

Así, un mismo HTML puede mostrar:

- únicamente hechos muy sólidos;
- hechos más periodismo documentado;
- inferencias;
- hipótesis;
- el “crazy wall” completo.

El control visual de rigor permite desplazarse entre esos universos sin confundirlos.

## 3.1 Principio de núcleo y periferia

El grafo debe imaginarse como un sistema con un **núcleo de alta confianza** y una **periferia progresivamente más especulativa**.

La periferia no está prohibida. Al contrario, es útil para descubrir preguntas. Pero debe permanecer claramente diferenciada.

La meta no es eliminar la especulación, sino **hacerla trazable, falsable y visualmente imposible de confundir con un hecho**.

# 4. Unidad fundamental: nodo, arista, fuente, evento e hipótesis

El sistema se organiza en cinco objetos lógicos principales:

1. **Nodo:** algo que existe o se modela como entidad del universo.
2. **Arista:** una relación específica entre dos nodos.
3. **Fuente:** evidencia documental o informativa que sustenta una afirmación.
4. **Evento:** algo ocurrido en una fecha o periodo que puede vincular múltiples nodos.
5. **Hipótesis:** una explicación estructurada que conecta patrones y genera predicciones verificables.

Cada objeto debe tener un identificador estable y un historial de cambios en Git.

# 5. Ontología de nodos

Los tipos mínimos recomendados son:

- `person`: persona física relevante por cargo, actividad empresarial, investigación, testimonio, operación o relación material.
- `org`: institución pública, partido, autoridad, dependencia, organismo internacional, organización criminal u otra organización.
- `company`: empresa, sociedad, vehículo corporativo, fideicomiso o entidad mercantil.
- `project`: obra pública, megaproyecto, infraestructura, concesión o programa.
- `event`: decomiso, captura, extradición, sanción, revocación, renuncia, asesinato, fuga, accidente, auditoría, filtración, cambio de propiedad, etc.
- `place`: puerto, aduana, terminal, inmueble, región, aeropuerto, corredor logístico u otro espacio geográfico relevante.
- `asset`: buque, aeronave, propiedad, cuenta, contrato, concesión, permiso, patente, activo o instrumento específico cuando sea analíticamente útil.
- `document`: expediente, auditoría, contrato, oficio, filtración, indictment, sanción, resolución o pieza documental central.
- `concept`: ecosistema analítico como “huachicol fiscal”, “financiamiento político”, “militarización aduanera” o “contrabando marítimo”; no representa una entidad jurídica.

## 5.1 Campos recomendados del nodo

Todo nodo debería poder registrar, cuando corresponda:

- `id` estable;
- nombre canónico;
- aliases o nombres alternativos;
- tipo de nodo;
- descripción neutral y breve;
- fechas de actividad relevantes;
- localización o jurisdicción;
- temas o comunidades asociadas;
- primera y última fecha de aparición en el corpus;
- estado: activo, histórico, fallecido, disuelto, desconocido, etc.;
- fuentes básicas de identidad;
- notas de desambiguación;
- sensibilidad o restricciones de privacidad, si procede.

# 6. Ontología de aristas

Una arista es una **afirmación**. Debe poder responder: “¿qué relación concreta afirmamos entre A y B, con qué fuerza y basado en qué?”.

Campos mínimos:

- `id`: identificador estable;
- `a`, `b`: nodos extremos;
- `g`: grado epistemológico A–G;
- `rel`: descripción corta de la relación;
- `why`: explicación de qué evidencia la sustenta;
- `src`: fuentes que sostienen específicamente esa relación.

Campos recomendados para ampliar:

- dirección de la relación si importa;
- fecha inicial y final;
- tipo: familiar, laboral, contractual, financiero, corporativo, político, institucional, logístico, testimonial, judicial, geográfico, etc.;
- monto, volumen o activo, si es relevante;
- jurisdicción;
- hipótesis asociadas;
- evidencia contradictoria;
- fecha de última revisión;
- analista/PR de origen;
- grado previo, para trazabilidad.

## 6.1 Regla de oro de la arista

> **La fuente debe demostrar la arista, no simplemente mencionar ambos nodos por separado.**

Si una nota menciona a X en un párrafo y a Y en otro, pero no establece relación entre X y Y, no puede utilizarse para crear una arista directa X–Y.

# 7. Escala epistemológica A–G

La escala A–G clasifica **la fuerza de una relación**, no el prestigio de una fuente ni la moralidad de los actores.

## A — Confirmado / evidencia primaria

Relación establecida por evidencia primaria suficientemente sólida, por ejemplo:

- nombramiento oficial;
- parentesco público inequívoco;
- contrato o convenio auténtico;
- registro mercantil;
- resolución administrativa;
- documento judicial;
- sentencia;
- sanción oficial;
- declaración directa verificable;
- acto institucional no controvertido.

A no significa que todo lo dicho sobre un actor sea cierto. Significa que **esa arista concreta** está establecida.

## B — Fuertemente documentado

La relación está respaldada por múltiples fuentes confiables, documentos identificables o una investigación periodística robusta cuya base documental puede rastrearse, pero no contamos todavía con el documento primario completo o la confirmación equivalente a A.

## C — Reportado / alegado

La relación proviene de:

- investigación periodística;
- denuncia;
- testimonio;
- expediente parcial;
- fuente atribuida;
- declaración de una parte;
- documento cuya interpretación aún requiere corroboración.

Debe expresarse siempre con lenguaje de atribución: “según”, “reportó”, “alega”, “el expediente señala”, etc.

## D — Inferido

La relación no está explícitamente afirmada por una fuente. Se deduce de hechos distintos.

Toda arista D debe explicar el razonamiento que la produce y, preferentemente, qué dato permitiría confirmarla o descartarla.

## E — Hipótesis investigable

Conexión explícitamente propuesta para ser investigada. Debe generar predicciones, posibles documentos, intermediarios o huellas que puedan buscarse.

Una E sin forma razonable de falsación no debería permanecer como E; puede degradarse a F o G.

## F — Conspirativo

Hipótesis que requiere **varios supuestos no demostrados**, actores ocultos, coordinación no documentada o interpretación de múltiples anomalías como parte de una arquitectura común.

F es una categoría permitida y deliberada del proyecto. Su función es explorar escenarios que una investigación convencional podría no formular, pero **nunca debe mostrarse como hecho**.

## G — Wildcard

Asociación, coincidencia, anomalía o posibilidad remota que todavía carece de una cadena causal razonable. Se conserva porque en una ola futura podría aparecer un puente inesperado.

Una G puede convertirse en evidencia útil o desaparecer del mapa. Ninguno de los dos resultados es un fracaso.

# 8. Escala de calidad de fuentes: separada de A–G

No debe confundirse la fuerza de una arista con la calidad de su fuente. Para evitar colisión de nomenclaturas, se recomienda clasificar fuentes con **S1–S4**.

## S1 — Fuente primaria / oficial

Ejemplos:

- FGR, UIF, SAT, ASF, SFP/Secretaría Anticorrupción;
- DOF, Compranet y plataformas oficiales de contratación;
- Pemex, ANAM, Sedena, Semar;
- registros mercantiles y de propiedad cuando sean legítimamente accesibles;
- tribunales y expedientes judiciales;
- DOJ, Treasury/OFAC/FinCEN, State Department, DEA/HSI/FBI/CBP cuando publiquen documentación;
- contratos, escrituras, actas corporativas, permisos, auditorías, sanciones, resoluciones y declaraciones directas verificables.

## S2 — Secundaria de alta calidad

Periodismo con estándares profesionales, atribución clara y, preferentemente, documentación:

- Reuters;
- Associated Press;
- Financial Times;
- El País;
- Le Monde;
- Aristegui Noticias;
- Animal Político;
- Mexicanos Contra la Corrupción y la Impunidad;
- Proceso, Reforma u otros medios cuando la pieza concreta tenga soporte documental.

La inclusión en S2 no significa que toda publicación del medio sea correcta. Se evalúa **artículo por artículo**.

## S3 — Secundaria útil pero de corroboración necesaria

Medios locales, sectoriales, análisis especializados, ONG, declaraciones políticas o investigaciones con documentación parcial. Pueden sostener una pista o una arista C, pero se debe buscar corroboración.

## S4 — Lead generation

Redes sociales, videos, publicaciones partidistas, cuentas anónimas, rumores, capturas sin procedencia clara y agregadores.

S4 **no debe utilizarse como evidencia final** para una afirmación reputacional seria. Sirve para generar términos de búsqueda, nombres, fechas, sociedades o documentos que después deben verificarse.

# 9. Protocolo de atribución y lenguaje

Este proyecto trata con personas reales, acusaciones criminales y asuntos reputacionalmente sensibles. Por ello:

- una acusación no se transforma en hecho por repetirse en muchos medios;
- una investigación abierta no equivale a culpabilidad;
- un indictment es una acusación, no una sentencia;
- una visa revocada no es prueba de delito;
- una sanción administrativa debe describirse exactamente por lo que sanciona;
- un testimonio de testigo protegido requiere atribución y corroboración;
- una relación familiar o de amistad no implica complicidad;
- un contrato público no implica corrupción por sí mismo;
- una coincidencia temporal no implica causalidad.

Formulaciones preferidas:

- “Reuters reportó que…”
- “Según el expediente citado por…”
- “La FGR afirmó que…”
- “El DOJ alega en la acusación…”
- “No existe evidencia pública que establezca…”
- “Esto no demuestra que…”
- “La conexión permanece en grado C/F hasta obtener…”

# 10. Alcance temporal y geográfico

Periodo base: **2018–2026**.

Se permite y recomienda retroceder antes de 2018 cuando un nodo, sociedad, relación empresarial, red criminal, historial político o infraestructura tenga antecedentes necesarios para explicar el periodo principal.

El universo es México, pero la investigación debe extenderse transnacionalmente cuando existan conexiones con:

- Estados Unidos;
- Panamá y otros registros corporativos;
- rutas marítimas;
- intermediarios financieros;
- proveedores extranjeros;
- extradiciones;
- sanciones;
- comercio exterior;
- empresas o jurisdicciones relevantes.

# 11. Corpus de investigación

La investigación debe combinar búsqueda temática y expansión por grafo.

## 11.1 Fuentes mexicanas prioritarias

- FGR;
- UIF;
- SAT;
- ASF;
- SFP/Secretaría Anticorrupción y Buen Gobierno;
- Sedena;
- Semar;
- Pemex;
- ANAM;
- DOF;
- Compranet y plataformas de contratación;
- registros corporativos y de propiedad legítimamente accesibles;
- fiscalías y gobiernos estatales cuando sean relevantes.

## 11.2 Fuentes estadounidenses prioritarias

- DOJ;
- Treasury / OFAC / FinCEN;
- State Department;
- DEA;
- HSI;
- FBI;
- CBP;
- tribunales federales;
- expedientes de extradición;
- documentos de sanciones y decomisos.

## 11.3 Periodismo prioritario

Reuters, AP, FT, El País, Le Monde, Aristegui, Animal Político, MCCI, Proceso, Reforma y otros medios con documentación verificable.

## 11.4 Estrategia bilingüe

Para asuntos transfronterizos se debe buscar en español e inglés. Un caso puede estar descrito de forma muy distinta en prensa mexicana, documentos de EE. UU. y registros corporativos.

# 12. Registro de eventos

Un evento debe capturar, cuando sea posible:

- fecha exacta o periodo;
- actores;
- localización;
- institución o empresa;
- descripción neutral del evento;
- fuentes;
- calidad de fuente S1–S4;
- tipo de evidencia;
- monto, volumen o activo;
- nodos relacionados;
- aristas que crea o modifica;
- explicación alternativa;
- grado de anomalía;
- estado: verificado, reportado, alegado, especulativo, contradicho o cerrado.

La fecha de publicación de una nota y la fecha en que ocurrió el evento deben almacenarse separadamente cuando difieran.

# 13. Protocolo de anomalías

Una **anomalía** no es un delito. Es un patrón que merece atención porque se aparta de lo esperado y puede ayudar a priorizar investigación.

Ejemplos:

- empresa constituida poco antes de recibir contratos relevantes;
- adquisición patrimonial inusual;
- cambios societarios próximos a un evento político o regulatorio;
- renuncia o nombramiento inesperado;
- expansión abrupta de importaciones;
- desaparición de una investigación;
- decomiso de escala excepcional;
- cambio de propietarios después de una investigación;
- muerte, asesinato, fuga o desaparición de un operador;
- contradicción entre una narrativa oficial y documentación contemporánea;
- repetición del mismo intermediario en redes aparentemente independientes;
- coincidencias logísticas, corporativas o financieras que requieren explicación.

## 13.1 Anomaly Score 0–5

La puntuación sirve para priorizar, no para asignar culpabilidad.

- **0:** comportamiento ordinario o explicado.
- **1:** curiosidad menor.
- **2:** irregularidad moderada con explicación plausible.
- **3:** anomalía clara que merece seguimiento.
- **4:** patrón difícil de explicar con información disponible.
- **5:** convergencia de varias anomalías o contradicciones que justifica una ola específica.

Factores orientadores:

- proximidad temporal;
- magnitud financiera o logística;
- secuencia inusual;
- repetición de intermediarios;
- contradicción con declaraciones públicas;
- ausencia de explicación normal suficiente.

> **Un Anomaly Score alto jamás debe presentarse como probabilidad de delito.**

# 14. Protocolo de olas de investigación

Las olas son ciclos de expansión controlada del universo. Cada ola debe responder una pregunta clara y terminar con un PR auditable.

## Ola 0 — Sistema y ontología

Objetivo: construir las reglas antes de acumular datos.

Define:

- tipos de nodos;
- tipos de aristas;
- escala A–G;
- clasificación de fuentes;
- estructura JSON;
- reglas de hipótesis;
- convención de IDs;
- visualización;
- gobernanza Git;
- validaciones.

## Ola 1 — Núcleo López Obrador

Mapear sin pretender demostrar una conspiración:

- Andrés Manuel López Obrador;
- Andrés Manuel López Beltrán;
- Gonzalo López Beltrán;
- José Ramón López Beltrán;
- relaciones familiares, políticas, empresariales, patrimoniales y públicas relevantes;
- amigos, colaboradores, compañías, proyectos y controversias documentadas.

El objetivo es generar un **núcleo factual**, no una acusación.

## Ola 2 — Primer círculo / expansión por vecino

Cada nodo relevante de Ola 1 se investiga **como universo independiente**.

Ejemplo conceptual:

`hijo de AMLO → empresario cercano`

La siguiente pregunta ya no es “¿qué hay sobre el hijo?”, sino:

> “¿Cuál es el universo corporativo, contractual, financiero, familiar, logístico e institucional del empresario?”

Se buscan:

- sociedades;
- accionistas;
- administradores;
- apoderados;
- contadores;
- domicilios corporativos;
- notarios;
- contratistas;
- proveedores;
- clientes;
- cambios societarios;
- contratos;
- permisos;
- importaciones/exportaciones;
- litigios e investigaciones.

## Ola 3 — Ecosistemas

La investigación deja de centrarse en personas y construye sistemas completos:

- huachicol y huachicol fiscal;
- aduanas;
- Pemex;
- puertos;
- Dos Bocas;
- Tren Maya;
- Corredor Interoceánico;
- Sedena;
- Marina;
- Tabasco;
- Tamaulipas;
- financiamiento político;
- contratación pública;
- empresas fachada;
- sistema financiero;
- carteles;
- Estados Unidos.

Se incorporan actores aunque **no parezcan conectados inicialmente con la familia López Obrador**.

## Ola 4 — Anomalías

Se incorporan deliberadamente eventos extraños o periféricos:

- muertes y asesinatos;
- fugas y desapariciones;
- renuncias y nombramientos;
- decomisos;
- visas revocadas;
- sanciones;
- extradiciones;
- filtraciones;
- auditorías archivadas o retrasadas;
- accidentes de megaproyectos;
- incendios;
- adquisiciones patrimoniales;
- empresas creadas antes de contratos;
- cambios de dueños;
- buques, vuelos o rutas inusuales.

Estos eventos entran como nodos **sin forzar todavía una explicación común**.

## Ola 5 — Investigación inversa / graph-driven research

A partir de aquí el propio grafo ayuda a decidir qué investigar.

Se priorizan nodos que:

- conectan varias comunidades;
- tienen betweenness elevado;
- aparecen en rutas diferentes;
- comparten domicilios, administradores o proveedores con múltiples redes;
- son intermediarios aparentemente secundarios pero estructuralmente importantes.

La pregunta cambia de “¿qué actor famoso investigamos?” a:

> “¿Qué nodo, si se explica, reduce más incertidumbre en el universo?”

## Ola 6 — Estados Unidos y dimensión transnacional

Reconstruir el universo documental de:

- Treasury/OFAC;
- FinCEN;
- DOJ;
- DEA;
- HSI;
- FBI;
- CBP;
- tribunales federales;
- sanciones;
- indictments;
- extradiciones;
- empresas estadounidenses;
- intermediarios fronterizos;
- rutas comerciales;
- visas, sólo en la medida en que haya información pública.

Luego se observa dónde este universo toca el mexicano.

## Ola 7 — Espacio conspirativo

No significa abandonar rigor. Significa preguntar explícitamente:

> **¿Qué estructura invisible podría producir el patrón visible?**

Aquí se permiten hipótesis audaces, incluidas conexiones de tres, cinco o más saltos, siempre que cada salto conocido tenga evidencia y cada salto faltante esté identificado como tal.

## Ola 8 — Red team y falsificación

Toda hipótesis importante debe ser atacada activamente.

Se busca:

- evidencia que la contradiga;
- casos comparables en otros partidos o administraciones;
- explicaciones sistémicas no conspirativas;
- errores de cronología;
- relaciones ordinarias de mercado;
- confusión entre actores con nombres similares;
- selección sesgada de noticias;
- hechos independientes conectados narrativamente por medios o analistas.

# 15. Regla de cadenas multi-hop

El proyecto está diseñado para descubrir conexiones indirectas. Una cadena larga **no es un problema** si cada arista está sustentada.

Ejemplo abstracto:

`Persona A → Persona B → Empresa C → Empresa D → Aduana E → Operador F → Evento G`

Puede ser más interesante que una conexión directa.

Sin embargo:

> **Una cadena dramática no es evidencia si uno de sus puentes centrales es imaginario.**

Cuando una teoría depende de una sola arista débil:

`A ━ B ━ C ━ D ···?··· E ━ F ━ G`

el objetivo prioritario de la siguiente investigación debe ser **D–E**.

El sistema debe permitir ver qué hipótesis colapsan si una determinada arista desaparece.

# 16. Investigación de puentes

Los “puentes ocultos” pueden ser mucho menos llamativos que los actores famosos. Buscar especialmente:

- empresas intermedias;
- abogados;
- contadores;
- notarios;
- apoderados;
- domicilios corporativos;
- socios repetidos;
- proveedores de segundo o tercer nivel;
- agentes aduanales;
- transportistas;
- buques;
- terminales;
- concesiones;
- permisos;
- cuentas o instituciones financieras cuando existan datos legítimos;
- funcionarios de nivel medio;
- fechas de transición;
- empresas recién constituidas;
- cambios de razón social;
- beneficiarios controladores cuando sean públicamente verificables.

# 17. Hipótesis: estructura obligatoria

Cada hipótesis debe tener un ID estable, por ejemplo `H01`, `H02`, etc.

Debe registrar:

1. **Enunciado:** qué sostiene exactamente.
2. **Alcance:** qué explica y qué no pretende explicar.
3. **Evidencia favorable:** hechos o patrones que aumentan su plausibilidad.
4. **Evidencia contraria:** hechos que la debilitan.
5. **Supuestos necesarios:** qué tendría que ser cierto sin estar demostrado.
6. **Aristas críticas:** conexiones cuya caída destruye o modifica la hipótesis.
7. **Predicciones:** qué esperaríamos encontrar si fuera correcta.
8. **Pruebas de falsación:** qué hallazgo la reduciría sustancialmente.
9. **Alternativas:** hipótesis rivales que explican el mismo patrón.
10. **Estado:** abierta, fortalecida, debilitada, parcialmente falsada, descartada o absorbida por otra.
11. **Última revisión:** fecha y PR.

# 18. Universo inicial de hipótesis rivales

Estas hipótesis son **familias analíticas**, no conclusiones. Pueden dividirse, combinarse o descartarse.

## H0 — Economía criminal sistémica y descentralizada

Las anomalías se explican principalmente por múltiples redes criminales y corruptas sin mando político común.

## H1 — Corrupción múltiple facilitada por controles débiles

Diversas redes independientes prosperaron bajo debilidades institucionales, opacidad y reorganización de funciones públicas.

## H2 — Red político-empresarial alrededor de algunos hijos de AMLO

Existe una red de influencia o beneficios empresariales alrededor de personas cercanas a algunos hijos, independiente o parcialmente independiente de redes de huachicol.

## H3 — Superposición entre red empresarial de los hijos y red de combustible/aduanas

Existe un puente real entre ambos universos. **Esta hipótesis requiere demostrar puentes concretos y no puede inferirse por amistad o proximidad.**

## H4 — Financiamiento político y economías de huachicol se superponen

Algunas redes de combustible pudieron financiar política o campañas mediante operadores regionales sin que ello implique necesariamente dirección familiar o presidencial.

## H5 — Red transversal a partidos y gobiernos

Huachicol, aduanas, empresas fachada y corrupción forman un ecosistema donde participan actores de distintos partidos y administraciones.

## H6 — Estados Unidos posee inteligencia no pública

Autoridades estadounidenses podrían disponer de información financiera, testimonial, judicial o de inteligencia aún no publicada y utilizar primero herramientas administrativas o sancionatorias.

## H7 — Herramientas de seguridad como presión geopolítica

EE. UU. puede combinar preocupaciones de seguridad reales con instrumentos de negociación política, comercial o diplomática.

## H8 — Guerra de facciones mexicanas

Actores internos filtran, proporcionan o amplifican información para debilitar a facciones rivales, incluidas facciones dentro del mismo partido.

## H9 — Conducta real + explotación política oportunista

Puede existir conducta irregular real y, simultáneamente, explotación política doméstica o internacional de esos hechos.

## H10 — Narrativa mediática de gran conspiración

Eventos reales pero independientes pueden estar siendo unidos selectivamente hasta producir la apariencia de una arquitectura centralizada inexistente.

## H11 — Debilidad institucional y sesgo de selección

Gran parte de las anomalías puede explicarse por incentivos de corrupción, penetración criminal, instituciones débiles y selección de noticias llamativas, sin conspiración central.

# 19. Evaluación estructurada de hipótesis

Se recomienda puntuar cada hipótesis en cinco dimensiones de 0 a 5:

- **Evidencia favorable**: 0–5.
- **Cobertura explicativa**: 0–5.
- **Supuestos requeridos**: 0–5, donde 0 significa pocos supuestos y 5 demasiados.
- **Consistencia con contraevidencia**: 0–5.
- **Falsabilidad/predicciones**: 0–5.

Puede construirse un **índice heurístico 0–100**:

`4 × [evidencia + cobertura + (5 − supuestos) + consistencia + falsabilidad]`

Este número sirve para comparar hipótesis dentro del proyecto. **No es una probabilidad estadística ni un posterior bayesiano.**

Sólo debe utilizarse la expresión “probabilidad bayesiana” si se han especificado priors, likelihoods y un modelo cuantitativo legítimo. En los demás casos debe hablarse de **plausibilidad heurística** o **análisis de hipótesis competidoras**.

# 20. Red team: protocolo obligatorio

El red team no es una fase opcional reservada al final. Debe aparecer durante toda la investigación.

Por cada hipótesis importante preguntar:

- ¿Qué evidencia esperamos si es correcta?
- ¿Qué observación sería extraña si es correcta?
- ¿Qué evidencia la mataría?
- ¿Qué explicación más simple compite con ella?
- ¿Existe un caso equivalente bajo PAN, PRI u otra fuerza que indique un fenómeno sistémico?
- ¿Estamos seleccionando sólo hechos compatibles?
- ¿La secuencia temporal permite la causalidad propuesta?
- ¿Una relación puede ser comercial, familiar o burocrática ordinaria?
- ¿La fuente tiene incentivos políticos o legales para exagerar?
- ¿Una acusación fue después retirada, negada o contradicha?

La evidencia exculpatoria, contradictoria o normalizadora debe entrar al grafo con la misma disciplina que la evidencia incriminatoria.

# 21. Tiempo, secuencia y causalidad

El grafo debe integrar una dimensión temporal fuerte.

Secuencias que merecen exploración:

`Evento A → 12 días → nombramiento B → 3 meses → contrato C → 8 meses → cambio societario D → investigación E → salida del país F`

La secuencia puede representar:

- coincidencia;
- consecuencia normal;
- reacción;
- adaptación;
- encubrimiento hipotético;
- o ausencia total de relación.

La cronología **no demuestra causalidad**, pero puede invalidarla. Si B ocurrió antes de A, una hipótesis que exige A→B debe revisarse.

Toda ruta causal importante debe ser **temporalmente posible**.

# 22. Métodos de análisis de red

La visualización cinematográfica debe coexistir con análisis computacional.

## 22.1 Degree centrality

Cuenta conexiones directas. Útil para actores muy conectados, pero puede sobrevalorar instituciones grandes o nodos genéricos.

## 22.2 Weighted degree

Pondera las conexiones según confianza, tipo o relevancia. Un nodo con diez aristas F no debería necesariamente parecer más sólido que uno con cinco A/B.

## 22.3 Betweenness centrality

Detecta nodos que funcionan como puentes entre comunidades. Es especialmente importante para encontrar intermediarios aparentemente secundarios.

## 22.4 Comunidades

Algoritmos de detección de comunidades pueden revelar “islas” temáticas: empresarial, aduanera, financiera, política, criminal, internacional, etc.

## 22.5 Caminos mínimos

Permiten preguntar “¿qué rutas conectan X con Y?”. Deben utilizarse para **generar preguntas**, nunca como argumento automático de culpabilidad.

## 22.6 Nodos de articulación y puentes

Identificar qué nodo o arista, al eliminarse, separa dos regiones del grafo. Son candidatos prioritarios para investigación porque muchas hipótesis pueden depender de ellos.

## 22.7 Rutas temporalmente válidas

Una ruta debe poder filtrarse por fechas para evitar conexiones imposibles o anacrónicas.

# 23. Islas temáticas iniciales

El grafo puede organizarse visualmente en islas que después se conectan o permanecen independientes.

Ejemplos de islas de investigación:

## Familia / López Beltrán

AMLO, Andrés Manuel López Beltrán, Gonzalo López Beltrán, José Ramón López Beltrán, amistades empresariales, negocios públicos conocidos y controversias documentadas.

## Huachicol / combustible

Empresas, transportistas, puertos, aduanas, buques, agentes, carteles, Pemex y decomisos.

## Marina / Sedena / Aduanas

Reorganización institucional, mandos, puertos, aduanas terrestres y marítimas, investigaciones y decomisos.

## Megaproyectos

Dos Bocas, Tren Maya, Corredor Interoceánico, proveedores, balasto, terrenos, contratos y supervisión.

## Tabasco

Poder político estatal, seguridad pública, redes criminales, La Barredora y economías de combustible.

## Tamaulipas / frontera

Puertos, aduanas, contrabando, operadores empresariales, redes de huachicol y financiamiento político alegado.

## Financiero

Casas de bolsa, bancos, UIF, transferencias, empresas fachada, OFAC/FinCEN y operaciones sospechosas documentadas.

## Estados Unidos

Visas, sanciones, DOJ, Treasury, DEA/HSI/FBI, extradiciones, empresas estadounidenses y rutas transfronterizas.

La pregunta central es:

> **¿Existen puentes documentables entre islas que hasta ahora parecen separadas?**

# 24. Visualización HTML: Intelligence Link Analysis

El archivo `index.html` es la interfaz del universo. Los datos deben permanecer, en lo posible, separados en JSON para que las investigaciones modifiquen el conocimiento sin reescribir el motor.

Funciones objetivo:

- zoom y desplazamiento;
- arrastre de nodos;
- búsqueda;
- filtros por tipo de nodo;
- filtros por temática;
- filtros por fechas;
- filtro por grado A–G;
- botón de vista factual;
- botón o modo “Crazy wall”;
- selección de dos nodos y cálculo de rutas;
- expansión de vecinos a N saltos;
- comunidades;
- centralidad y nodos puente;
- cronología;
- panel de detalle de nodo;
- panel de detalle de arista;
- acceso a fuentes;
- hipótesis asociadas;
- contradicciones;
- historial o procedencia del PR cuando sea posible.

## 24.1 Semántica visual sugerida

- línea sólida: relación demostrada/documentada;
- línea discontinua: relación indirecta o inferida;
- doble línea: vínculo financiero/comercial cuando el diseño lo permita;
- flecha: flujo de dinero, influencia, decisión, información o bienes cuando exista dirección demostrable;
- `?`: hipótesis;
- `X`: relación investigada y debilitada/contradicha;
- intensidad u opacidad: puede reflejar A–G, pero siempre acompañada de leyenda.

Los colores no deben ser la única forma de codificar confianza; deben existir etiquetas textuales por accesibilidad y claridad.

## 24.2 Panel de arista

Al seleccionar una relación, mostrar como mínimo:

- nodos extremos;
- relación;
- grado A–G;
- por qué existe;
- qué NO demuestra;
- fechas;
- fuentes;
- contradicciones;
- hipótesis afectadas;
- PR o revisión de origen.

## 24.3 Control de rigor

Conceptualmente:

`HECHOS ━━━━━━━━━━━━━━━━━ CONSPIRACIÓN`

El extremo factual debe dejar sólo A y, opcionalmente, B. Al desplazarse se agregan C, D, E, F y G.

El objetivo es que el usuario pueda observar **cómo una narrativa especulativa emerge de un núcleo factual** y cuáles son sus puentes débiles.

# 25. Estructura del repositorio

Arquitectura recomendada:

```text
Diagrama-Inteligencia-Mexico/
│
├── index.html
├── data/
│   ├── nodes.json
│   ├── edges.json
│   ├── sources.json
│   ├── hypotheses.json
│   └── timeline.json
│
├── research/
│   ├── wave-XX-topic/
│   └── ...
│
├── docs/
│   ├── PROTOCOLO_MAESTRO.md
│   ├── methodology.md
│   ├── ontology.md              # futuro si se separa
│   └── evidence-scale.md        # futuro si se separa
│
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
│
└── README.md
```

La estructura puede evolucionar. Si cambia, debe actualizarse este protocolo.

# 26. Git como parte de la metodología de inteligencia

GitHub no es sólo almacenamiento. Es el mecanismo de trazabilidad epistemológica.

Cada cambio relevante debería poder responder:

- ¿cuándo apareció esta arista?
- ¿qué fuente la originó?
- ¿qué grado tenía inicialmente?
- ¿quién o qué ola la modificó?
- ¿por qué subió o bajó de confianza?
- ¿qué hipótesis dependían de ella?

Por eso el historial de PR es parte de la evidencia metodológica.

# 27. Convención de ramas y Pull Requests

Ramas recomendadas:

- `agent/wave-02-amilcar-olan`
- `agent/wave-03-portacelis-ikon`
- `agent/wave-04-customs-navy`
- `agent/wave-06-us-enforcement`
- `agent/red-team-h03`
- `agent/infra-graph-validation`

## 27.1 Contenido mínimo de un PR de investigación

El cuerpo del PR debe explicar:

1. pregunta de investigación;
2. corpus consultado;
3. nodos añadidos/modificados;
4. aristas añadidas;
5. aristas elevadas o degradadas;
6. fuentes nuevas;
7. contradicciones relevantes;
8. hipótesis fortalecidas/debilitadas;
9. puentes faltantes;
10. validaciones ejecutadas;
11. riesgos de interpretación.

## 27.2 Regla de `main`

`main` representa el **universo maestro estable**.

Una ola no debe considerarse incorporada hasta que su PR sea revisado y fusionado.

# 28. CI y validación automática

GitHub Actions debe evolucionar de un simple deploy a un **control de calidad del conocimiento**.

Validaciones recomendadas antes de publicar:

- todos los JSON son sintácticamente válidos;
- IDs de nodos únicos;
- IDs de aristas únicos;
- toda arista referencia nodos existentes;
- toda fuente citada existe en `sources.json`;
- grados sólo pertenecen a A–G;
- A–C tienen al menos una fuente;
- A requiere, idealmente, una fuente primaria o justificación explícita;
- D–G contienen explicación de inferencia/hipótesis;
- no hay fechas imposibles;
- no hay aliases que creen duplicados obvios;
- hipótesis referencian aristas existentes;
- URLs de fuentes tienen estructura válida;
- campos obligatorios no están vacíos.

Una mejora futura es producir métricas automáticas del grafo y un reporte de calidad en cada PR.

# 29. GitHub Pages y publicación

La visualización se despliega mediante GitHub Actions desde `main`.

Flujo esperado:

`PR → revisión → merge a main → validación → deploy → GitHub Pages actualizado`

La publicación del HTML no convierte los grados C–G en hechos. La interfaz debe preservar siempre las advertencias metodológicas.

# 30. Protocolo de privacidad y minimización

El proyecto se concentra en personas públicas, funcionarios, empresarios, empresas, operadores y actores materialmente relacionados con asuntos de interés público.

Reglas:

- no incluir teléfonos privados;
- no publicar domicilios residenciales exactos de personas privadas salvo que sean documentos públicos indispensables y exista una razón analítica clara; preferir ciudad/estado o domicilio corporativo;
- no mapear menores ni familiares sin relevancia pública directa;
- no incorporar información íntima irrelevante;
- evitar “doxxing”;
- distinguir domicilio corporativo público de vivienda privada;
- no incorporar a familiares únicamente por parentesco;
- minimizar información de personas periféricas no públicas.

# 31. Protocolo para muertes, asesinatos, accidentes y desapariciones

Estos eventos tienen gran poder narrativo y por ello requieren especial disciplina.

Nunca inferir automáticamente que:

- una muerte fue un silenciamiento;
- un accidente fue sabotaje;
- una desaparición estuvo vinculada a una investigación;
- un asesinato prueba que la víctima conocía determinada información.

Para conectarlos a una hipótesis se debe exigir:

- cronología compatible;
- relación previa demostrada;
- motivo o patrón documentable;
- corroboración independiente;
- explicación alternativa explícita.

Si sólo existe coincidencia temporal, el evento puede permanecer como G/Wildcard.

# 32. Protocolo para filtraciones y documentos hackeados

Filtraciones como Guacamaya pueden ser extremadamente útiles, pero requieren:

- verificar autenticidad cuando sea posible;
- diferenciar documento original, interpretación periodística y conclusión analítica;
- registrar fecha del documento y fecha de publicación;
- evitar extraer una frase sin contexto;
- buscar confirmación en fuentes oficiales o documentos posteriores;
- no elevar automáticamente un reporte de inteligencia a hecho judicial.

# 33. Protocolo para sanciones, causas judiciales y visas de EE. UU.

## Sanciones

Describir exactamente quién fue sancionado, bajo qué autoridad y por qué conducta alegada o determinada.

## Indictments / acusaciones

Usar lenguaje de presunción de inocencia. Un indictment es acusación formal, no condena.

## Extradiciones

Diferenciar solicitud, detención, resolución y entrega efectiva.

## Visas

La cancelación o revocación de una visa puede obedecer a múltiples bases y los expedientes suelen ser confidenciales. **No inferir motivo específico sin evidencia pública.**

Una coincidencia entre revocación de visa y una investigación criminal puede registrarse como pregunta, pero no como conexión probada.

# 34. Contradicciones y evidencia negativa

El grafo debe poder representar no sólo relaciones, sino **ausencias relevantes y contradicciones**.

Ejemplos:

- una autoridad declara no tener investigación contra una persona;
- un contrato supuesto no aparece en el registro esperado;
- una empresa niega relación y aporta documentación;
- una fecha vuelve imposible una hipótesis;
- un testigo se retracta;
- un proceso es desestimado;
- una auditoría concluye que no encontró determinada irregularidad.

La evidencia negativa debe bajar la confianza cuando corresponda.

# 35. Regla de no-centralidad y sesgo de confirmación

Nunca diseñar la búsqueda exclusivamente como:

> “encontremos cómo conectar a AMLO con X”.

La formulación correcta es:

> “construyamos el universo de X y observemos qué puentes aparecen”.

Si después aparece AMLO, uno de sus hijos, un opositor, un militar, un cartel o ninguna figura política, el resultado debe aceptarse.

# 36. Casos comparables como falsificación

Una de las herramientas más poderosas contra el sesgo es buscar redes similares fuera del grupo político inicialmente investigado.

Si encontramos:

- redes de huachicol vinculadas a PAN, PRI u otros actores;
- empresas fachada que operan bajo distintos gobiernos;
- corrupción aduanera transversal;
- mecanismos similares en administraciones anteriores;

entonces aumenta el peso de hipótesis sistémicas y disminuye el valor explicativo de “pertenecer a Morena” como variable causal por sí sola.

# 37. Criterio de incorporación de una noticia “extraña”

Una noticia periférica puede entrar si cumple al menos una de estas condiciones:

- involucra un nodo ya existente;
- involucra un intermediario compartido;
- ocurre en un lugar o infraestructura relevante;
- afecta una empresa relacionada;
- modifica una investigación, permiso, contrato o cargo;
- introduce un nuevo actor potencialmente puente;
- tiene anomaly score ≥ 3;
- podría falsar una hipótesis existente.

Puede entrar como evento G sin crear una arista causal.

# 38. Definition of Done de una ola

Una ola está lista para PR cuando:

- la pregunta quedó explícita;
- las búsquedas principales fueron cubiertas en español e inglés cuando aplica;
- las fuentes se registraron;
- se añadieron los nodos necesarios;
- cada arista tiene grado y justificación;
- las alegaciones están atribuidas;
- las contradicciones fueron buscadas, no sólo toleradas;
- las hipótesis afectadas fueron revisadas;
- los puentes débiles quedaron identificados;
- los JSON pasan validación;
- el HTML continúa cargando correctamente;
- el PR explica riesgos y límites.

# 39. Salida esperada de cada ola

Cada ola debe producir cuatro tipos de resultado:

## 39.1 Cambios al grafo

Nodos, aristas, fechas y fuentes.

## 39.2 Hallazgos narrativos

Qué patrones nuevos surgieron y por qué importan.

## 39.3 Hipótesis

Qué aumentó o disminuyó en plausibilidad.

## 39.4 Agenda siguiente

Qué arista, documento, empresa o intermediario sería más informativo investigar después.

# 40. Formato de una “tarjeta de arista”

**ID:**

**Nodo A:**

**Nodo B:**

**Relación:**

**Grado A–G:**

**Periodo:**

**Evidencia principal:**

**Fuentes:**

**Qué demuestra:**

**Qué NO demuestra:**

**Evidencia contradictoria:**

**Hipótesis afectadas:**

**Dato faltante más importante:**

**Última revisión / PR:**

# 41. Formato de una “tarjeta de hipótesis”

**ID:** Hxx

**Título:**

**Enunciado preciso:**

**Evidencia favorable:**

**Evidencia contraria:**

**Supuestos necesarios:**

**Aristas críticas:**

**Predicciones:**

**Qué la falsaría:**

**Hipótesis rivales:**

**Puntuación heurística:**

**Estado:**

**Próxima acción:**

# 42. Formato de una “tarjeta de fuente”

**ID:** Sxx

**Título:**

**Autor/Institución:**

**Fecha de publicación:**

**Fecha del hecho cubierto:**

**URL / referencia:**

**Tipo:** primaria / periodística / testimonial / registral / judicial / etc.

**Calidad S1–S4:**

**Nodos mencionados:**

**Aristas que sustenta:**

**Limitaciones:**

**Archivo/backup si existe:**

# 43. Formato de una “tarjeta de evento”

**ID:** EVT-xxxx

**Fecha:**

**Lugar:**

**Actores:**

**Descripción neutral:**

**Fuente(s):**

**Anomaly Score 0–5:**

**Relaciones conocidas:**

**Relaciones hipotéticas:**

**Explicaciones alternativas:**

**Hipótesis afectadas:**

# 44. Preguntas que el grafo debe poder contestar

Ejemplos:

- ¿Qué nodos conectan la isla de megaproyectos con la isla de huachicol?
- ¿Qué empresas comparten socios, administradores o domicilios?
- ¿Qué personas aparecen en tres o más comunidades?
- ¿Qué rutas conectan a un actor político con una empresa investigada y qué grado tiene cada salto?
- ¿Qué hipótesis dependen de una sola arista F?
- ¿Qué eventos preceden a cambios societarios o nombramientos?
- ¿Qué conexiones desaparecen al ocultar grados D–G?
- ¿Qué red permanece cuando sólo mostramos A–B?
- ¿Qué nodos tienen mayor betweenness pero poca notoriedad pública?
- ¿Qué investigaciones de EE. UU. tocan actores del grafo mexicano?
- ¿Qué evidencia contradice nuestras hipótesis más atractivas?

# 45. Prioridad de investigación: valor de información

No siempre debe investigarse el nodo con más noticias. Debe priorizarse el dato que más cambie el universo.

Alta prioridad:

- arista crítica de la que dependen varias hipótesis;
- empresa puente entre dos comunidades;
- beneficiario controlador desconocido;
- documento primario capaz de elevar C→A/B;
- contradicción capaz de degradar varias conexiones;
- fecha que valida o destruye una secuencia causal;
- proveedor o cliente que aparece repetidamente.

# 46. Regla de actualización de confianza

La confianza puede subir o bajar.

Ejemplos:

- `C → B`: aparece documentación independiente.
- `B → A`: se obtiene contrato, expediente o registro primario.
- `E → F`: la búsqueda no encuentra los puentes predichos.
- `F → G`: queda sólo coincidencia remota.
- `C → contradicha`: surge evidencia sólida en sentido contrario.

Nunca conservar un grado alto por apego a una hipótesis anterior.

# 47. Cómo tratar información no encontrada

“No encontramos evidencia” no equivale automáticamente a “la relación no existe”. Registrar:

- qué se buscó;
- en qué fuentes;
- con qué rango temporal;
- qué limitaciones tuvo el acceso;
- qué documento faltaría.

La ausencia de evidencia puede debilitar una hipótesis, especialmente cuando esa hipótesis predice que la evidencia debería ser pública y fácil de localizar.

# 48. Conducta esperada del asistente durante investigación

El asistente debe:

- investigar ampliamente;
- conectar puntos de manera creativa;
- formular hipótesis audaces;
- distinguir claramente hechos y especulación;
- citar fuentes de forma precisa;
- buscar contraevidencia;
- corregir errores sin defender respuestas anteriores;
- preferir documentos primarios cuando sea posible;
- informar incertidumbre;
- crear ramas/PRs temáticos;
- mantener el repositorio como fuente de verdad.

El asistente **no debe**:

- presentar rumores como hechos;
- ocultar evidencia contradictoria porque perjudique una hipótesis;
- inferir delito de amistad, parentesco o cercanía;
- inventar puentes faltantes;
- usar redes sociales como prueba definitiva;
- centrar el grafo artificialmente en AMLO;
- confundir correlación temporal con causalidad;
- usar puntuaciones heurísticas como probabilidades científicas.

# 49. Rutina de inicio de cada sesión de investigación

Antes de investigar:

1. Leer Protocolo Maestro.
2. Leer `README.md` actual.
3. Leer `data/hypotheses.json`.
4. Identificar los nodos y aristas relevantes a la ola.
5. Revisar PRs recientes.
6. Anotar qué conexiones se consideran actualmente A–G.
7. Definir pregunta y criterios de salida.
8. Realizar investigación pública actualizada.
9. Comparar hallazgos con el grafo, no con recuerdos del chat.

# 50. Rutina de cierre de cada sesión

Antes de terminar:

1. Asegurar que hallazgos importantes estén en el repo o en un PR.
2. Registrar nuevas fuentes.
3. Actualizar grados de aristas cuando corresponda.
4. Actualizar hipótesis afectadas.
5. Registrar contraevidencia.
6. Señalar puentes faltantes.
7. Dejar un resumen de continuidad en el PR.
8. No dejar conocimiento crítico únicamente en la conversación.

# 51. Protocolo de transferencia entre conversaciones

Cuando una conversación alcance su límite:

- no intentar transportar todo mediante memoria informal;
- fusionar o dejar claramente identificado el PR activo;
- actualizar el Protocolo Maestro sólo si cambió la metodología;
- actualizar `README.md` si cambió arquitectura o deployment;
- dejar las preguntas pendientes en el PR o issue correspondiente;
- en la conversación nueva, comenzar leyendo repo + protocolo.

El **estado del grafo** pertenece a JSON/Git; el **estado del razonamiento** debe resumirse en hipótesis, contradicciones y PRs.

# 52. Prompt de reanudación recomendado

Puede utilizarse este texto al iniciar una conversación nueva:

> Estamos continuando el proyecto **Diagrama Inteligencia México**. Lee primero el **Protocolo Maestro** y después consulta el repositorio `GustavoEEG/Diagrama-Inteligencia-Mexico`, especialmente `README.md`, `data/nodes.json`, `data/edges.json`, `data/sources.json`, `data/hypotheses.json`, `data/timeline.json` y los PR recientes. El objetivo no es demostrar una teoría predeterminada, sino construir un Intelligence Link Analysis 2018–2026 que mantenga hechos, reportes, inferencias, hipótesis y wildcards separados mediante la escala A–G. No centres el grafo artificialmente en AMLO; deja que la centralidad emerja. Investiga conexiones multi-hop, anomalías y puentes ocultos, pero exige evidencia para cada arista. Busca también contraevidencia y explicaciones sistémicas. Trabaja mediante una rama/PR temático y deja en el repositorio todo hallazgo que deba sobrevivir a esta conversación.

# 53. Estado de referencia al crear este protocolo

Al 19 de agosto de 2026, el proyecto ya cuenta con:

- repositorio público `GustavoEEG/Diagrama-Inteligencia-Mexico`;
- `index.html` como motor del tablero;
- archivos JSON separados para nodos, aristas, fuentes, hipótesis y cronología;
- despliegue de GitHub Pages mediante GitHub Actions;
- una semilla inicial de decenas de nodos y relaciones;
- escala epistemológica A–G;
- metodología inicial en `docs/methodology.md`;
- flujo de trabajo por Pull Requests.

**Este apartado es sólo una fotografía histórica. Para conocer el estado actual, consultar siempre `main` y los PR recientes.**

# 54. Principio final

El proyecto debe poder volverse más interesante **sin volverse menos riguroso**.

La libertad para explorar conspiraciones, anomalías, rutas de cinco o diez saltos y explicaciones no convencionales depende de una disciplina estricta:

> **cada nodo debe ser identificable, cada arista debe explicar por qué existe, cada fuente debe sostener la afirmación que se le atribuye, cada hipótesis debe poder ser atacada y cada cambio debe quedar versionado.**

El resultado ideal no es una gran teoría. El resultado ideal es un universo suficientemente bien estructurado para que podamos descubrir si existe una gran teoría, varias redes independientes, una mezcla de ambas o ninguna.

---

# Anexo A. Checklist rápido de una nueva arista

- [ ] Ambos nodos existen.
- [ ] La relación está formulada de manera específica.
- [ ] La fuente demuestra esa relación y no sólo menciona a ambos.
- [ ] El grado A–G es proporcional a la evidencia.
- [ ] La fecha es compatible.
- [ ] Se explicó qué NO demuestra.
- [ ] Se registró contraevidencia si existe.
- [ ] Las fuentes están en `sources.json`.
- [ ] No se introduce culpabilidad por asociación.
- [ ] Si es D–G, se identifica el dato que podría confirmarla o falsarla.

# Anexo B. Checklist rápido de una hipótesis

- [ ] Tiene ID estable.
- [ ] El enunciado es falsable o al menos reducible mediante evidencia.
- [ ] Se enumeró evidencia favorable.
- [ ] Se enumeró evidencia contraria.
- [ ] Se declararon supuestos.
- [ ] Se identificaron aristas críticas.
- [ ] Tiene predicciones.
- [ ] Tiene hipótesis rivales.
- [ ] La puntuación, si existe, está etiquetada como heurística.
- [ ] Su estado se revisó después de la última ola relevante.

# Anexo C. Checklist rápido de un PR de investigación

- [ ] Pregunta de la ola.
- [ ] Corpus y fuentes.
- [ ] Nuevos nodos.
- [ ] Nuevas aristas.
- [ ] Aristas elevadas/degradadas.
- [ ] Contradicciones.
- [ ] Hipótesis afectadas.
- [ ] Puentes faltantes.
- [ ] Validación JSON/grafo.
- [ ] Riesgos de interpretación.
- [ ] Próxima ola sugerida.

# Anexo D. Vocabulario de estados

**Hecho:** relación suficientemente demostrada.

**Reportado:** afirmación atribuida a una fuente secundaria.

**Alegado:** afirmación de una parte, testigo, expediente o autoridad aún no adjudicada.

**Inferido:** conclusión analítica derivada de varios hechos.

**Hipótesis:** explicación propuesta y falsable.

**Especulativo:** escenario que requiere supuestos relevantes no demostrados.

**Wildcard:** anomalía o asociación remota conservada para exploración futura.

**Contradicho:** evidencia relevante disminuye de forma significativa la relación o hipótesis.

**Descartado:** la evidencia disponible hace que mantener la conexión deje de ser analíticamente útil, sin afirmar imposibilidad metafísica.

# Anexo E. Regla mnemotécnica del proyecto

**Recolectar → verificar → conectar → etiquetar → desafiar → versionar → visualizar → volver a investigar.**
