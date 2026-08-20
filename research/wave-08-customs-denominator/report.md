# Ola 8 — Customs Denominator / Full Portacelis Pediment Set

**Corte:** 19 de agosto de 2026  
**Pregunta:** ¿podemos reconstruir un universo suficientemente completo de pedimentos y patentes aduanales de Portacelis para probar H13 —si los agentes usados por la empresa aparecen en investigaciones de combustible con frecuencia anormal?

## Respuesta corta

**No con OSINT abierto de forma metodológicamente defendible.**

La ola activa su criterio de salida. No se calcula una tasa de enriquecimiento y no se convierte el dato observado `3677 + 3830 + 3807` en una muestra estadística. Las fuentes abiertas disponibles describen universos diferentes y la infraestructura pública oficial no expone un histórico nominativo completo por contribuyente.

Esto no invalida los pedimentos/embarques individuales ya reproducidos. Invalida el salto de esas muestras a una proporción del universo.

## 1. Qué permite y qué no permite la fuente oficial

ANAM publica archivos de información de comercio exterior, pero advierte que la información identificable de contribuyentes está protegida por confidencialidad/secreto fiscal. También mantiene mecanismos para que el propio contribuyente solicite o consulte sus operaciones mediante autenticación.

Consecuencia analítica:

- podemos usar estadísticas agregadas y operaciones individuales que aparezcan legítimamente en fuentes públicas/comerciales;
- no podemos asumir que esas muestras constituyen **todos** los pedimentos de Portacelis;
- no podemos calcular una tasa de agentes investigados entre todos los agentes usados por Portacelis sin conocer el conjunto completo;
- ausencia en un proveedor comercial no demuestra ausencia en el universo aduanal.

## 2. Cuatro universos observables que no son directamente comparables

### MCCI

La investigación de MCCI reconstruye **444 operaciones** de Portacelis entre el 4 de febrero y el 11 de julio de 2025. Describe 435 movimientos ferroviarios, una primera operación carretera y ocho operaciones marítimas. Brownsville GTR y MG Energy concentran la mayor parte del volumen declarado reconstruido.

Este es el universo periodístico más amplio localizado, pero no se dispone de la base subyacente completa dentro del repositorio para auditar fila por fila todas las patentes.

### Panjiva

El perfil público/comercial de Portacelis expone un número menor de registros disponibles y permite reproducir operaciones concretas, entre ellas:

- Benbros → Portacelis → Matamoros → ferrocarril → patente 3830;
- Brownsville GTR → Portacelis → Nuevo Laredo → ferrocarril → patente 3677;
- MG Energy → Portacelis → Veracruz → marítimo → patente 3807.

Un `shipment record` de Panjiva no debe asumirse equivalente uno-a-uno a una `operación` de la reconstrucción de MCCI.

### N+

N+ reportó que Portacelis compró diésel a **cinco comercializadoras de Texas** y que, al revisar una ventana específica de la base de importadores, encontró **130 ferrotanques entre mayo y junio** por Nuevo Laredo y Matamoros. También señala que ciertas operaciones observadas documentalmente no aparecían en la base revisada.

Esto demuestra por qué una ventana de ferrotanques no constituye el universo completo febrero–julio ni incluye necesariamente todas las modalidades de transporte.

### ImportKey

ImportKey permite corroborar un subconjunto marítimo y muestra ocho embarques de MG Energy a Portacelis. Es útil para corroborar el corredor marítimo; no pretende reconstruir los movimientos ferroviarios mexicanos.

## 3. Resultado del Full Pediment Set

Las patentes reproducidas con suficiente trazabilidad continúan siendo:

- **3830** — Hantulio Ordóñez Juárez;
- **3677** — Juan Hermilo Chávez Rodríguez;
- **3807** — Irene Angelina León Zamora.

No se obtuvo en esta ola la patente del primer movimiento Ikon del 4 de febrero de 2025 de manera suficientemente reproducible.

Por tanto el conjunto observado de tres patentes **no es un censo** y no debe convertirse en denominador.

## 4. Universo de proveedores: cinco reportados, cuatro nominalmente reproducidos

N+ reporta cinco comercializadoras texanas proveedoras de Portacelis. En las fuentes indexadas disponibles pudimos reproducir cuatro nombres:

1. Ikon Midstream;
2. Brownsville GTR;
3. MG Energy;
4. Benbros Enterprises.

El quinto proveedor no fue identificado con soporte reproducible. No se crea un nodo de empresa desconocida y no se intenta inferir su identidad por descarte.

## 5. Decisión sobre H13

H13 preguntaba si los agentes aduanales utilizados por Portacelis estaban **enriquecidos** en investigaciones de combustible respecto de una tasa base.

La señal observada de Olas 6–7 sigue existiendo:

- 3677: su titular enfrenta proceso en la causa ferroviaria asociada a Ingemar;
- 3830: aparece en una investigación separada reportada por N+;
- 3807: no produjo en nuestras búsquedas una causa pública equivalente.

Sin embargo, `2 de 3` carece de significado inferencial porque:

- `n=3` es pequeño;
- las tres patentes no fueron muestreadas al azar;
- desconocemos si faltan otras patentes de Portacelis;
- desconocemos la tasa de investigaciones entre agentes comparables;
- no controlamos por número de pedimentos, cuota de mercado, aduana ni especialización;
- la cobertura judicial y mediática no es homogénea.

**Resultado:** H13 queda `No evaluable con OSINT abierto / estacionada`.

No se publica porcentaje, odds ratio, p-value ni puntuación de anomalía cuantitativa.

## 6. H14 — Sesgo de visibilidad y agregación aduanal

La ola formaliza una nueva hipótesis metodológica:

> **H14: la mezcla de fuentes con unidades, periodos y niveles de visibilidad diferentes puede crear falsas ausencias, dobles conteos o aparente enriquecimiento.**

Regla operativa añadida:

```text
muestra observable ≠ universo
shipment ≠ pedimento ≠ ferrotanque ≠ operación reconstruida
ausencia en una base ≠ ausencia en la realidad
```

Antes de cualquier análisis cuantitativo habrá que documentar para cada fuente:

- unidad de observación;
- cobertura temporal;
- cobertura geográfica/modal;
- regla de deduplicación;
- grado de completitud;
- restricciones de confidencialidad.

## 7. Lead de salida: supuesto oficio FEMDO de 353 objetivos de interés

Durante la búsqueda apareció una ruta potencialmente más valiosa que seguir ampliando la muestra aduanal.

Código Magenta afirma haber tenido acceso a un oficio de FEMDO fechado el **24 de septiembre de 2025**, dirigido a la titular del Centro Federal de Inteligencia Criminal, que enlistaría **353 personas, empresas y agencias** como objetos de interés de una investigación. Según el reportaje, entre las entidades mencionadas estarían **Portacelis, Ingemar e Ikon Midstream**.

La Ola 8 **no obtuvo el oficio primario** y no encontró una publicación oficial de FGR que reproduzca esa lista completa. Por ello:

- el documento se modela como `lead FEMDO · 353`;
- todas sus conexiones son **C — reportadas**;
- no se afirma que la inclusión implique imputación, responsabilidad o delito;
- una minuta de INEGI sólo corrobora independientemente el cargo de la funcionaria señalada como destinataria, no autentica el oficio ni su contenido.

Este lead puede ser mucho más informativo que seguir añadiendo pedimentos parciales porque, si el documento es auténtico y recuperable, ofrecería un universo explícito definido por una autoridad investigadora y permitiría comparar múltiples islas con un marco común.

## 8. H01 — Andy ↔ huachicol

**Sin avance material.**

La Ola 8 no encontró evidencia de que Andrés Manuel López Beltrán:

- seleccionara proveedores o agentes aduanales de Portacelis;
- aparezca en pedimentos;
- intervenga en trámites aduanales;
- reciba pagos o beneficios de estas operaciones;
- figure en el supuesto oficio FEMDO reportado.

No se altera la valoración de H01.

## 9. Criterio de salida y próxima dirección

El intento de `Full Portacelis Pediment Set` se detiene hasta contar con alguno de estos insumos:

- acceso autorizado al universo de operaciones de comercio exterior de la empresa;
- expediente SAT/ANAM que permita reconstruir todas las patentes;
- base periodística subyacente auditable con definición de unidad y deduplicación;
- conjunto completo obtenido mediante expediente judicial/documental público.

Seguir buscando ejemplos aislados tendría rendimientos decrecientes y aumentaría el riesgo de sesgo de selección.

La siguiente ola debe cambiar de isla y atacar el nuevo target documental:

> **verificar/adquirir el supuesto oficio FEMDO de 353 entidades y reconstruir si realmente crea una convergencia Portacelis–Ingemar–Ikon u otras redes.**

Si el oficio no existe, no puede autenticarse o el reportaje interpretó incorrectamente su contenido, el nodo debe debilitarse o eliminarse. Si se obtiene, cada inclusión deberá modelarse con su significado procesal exacto: `objeto de interés` no equivale a `imputado`, `investigado formalmente` ni `culpable`.
