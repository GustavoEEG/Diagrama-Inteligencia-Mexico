# Plan de adquisición documental — Ola 5

Este archivo convierte los huecos de evidencia del grafo en tareas documentales reproducibles.

## Regla

Un documento no se considera obtenido porque exista una captura, transcripción o referencia periodística. Registrar por separado:

- **identificador**;
- **custodio**;
- **vía de acceso**;
- **versión/corte**;
- **proveniencia**;
- **estado**: `TARGET`, `LEAD`, `OBTENIDO-NO-PRIMARIO`, `OBTENIDO-PRIMARIO`, `NO-LOCALIZADO`, `SELLADO/RESTRINGIDO`;
- hipótesis que puede fortalecer/debilitar.

---

## A. Registro Público de Comercio / SIGER

### Target A1 — Folio mercantil de Portacelis

- Entidad: Portacelis Gas & Oil, S.A. de C.V.
- RFC conocido en registros comerciales: `PGO240806CH8`
- FME reportado: `N-2024071962`
- NUD reportado: `2024002492590034`
- Custodio: Secretaría de Economía / Registro Público de Comercio / SIGER 2.0
- Estado: `OBTENIDO-NO-PRIMARIO` para copia espejo; `TARGET` para certificación oficial

### Recuperar

1. asiento de constitución de 6 ago 2024;
2. instrumento/notaría y administradores iniciales;
3. poder otorgado a Armando Carrillo Peregrino alrededor del 11 oct 2024;
4. asamblea/transmisión accionaria de 17 oct 2024;
5. cualquier revocación de poder;
6. modificaciones posteriores de administrador/comisario/accionistas/capital.

### Qué puede resolver

- H06 compartimentación corporativa;
- H08 continuidad operativa;
- H10 techo de fuente abierta;
- H11 continuidad regulatoria.

### Criterio de éxito

Certificación o boleta SIGER descargada directamente del sistema oficial, con metadatos verificables.

---

## B. SENER — permiso `1701C124002733`

### Target B1 — expediente individual del permiso

- Identificador: `1701C124002733`
- Custodio: Secretaría de Energía
- Estado: permiso **operativamente corroborado** en registros comerciales; expediente individual `TARGET`

### Recuperar

- solicitud original;
- resolución de otorgamiento;
- representante/apoderado que presentó el trámite;
- instrumento corporativo entregado;
- volumen autorizado;
- productos/fracciones;
- uso/destino;
- proveedores declarados;
- transportistas;
- terminales/instalaciones;
- clientes/usuarios finales;
- puntos de internación;
- modificaciones/avisos posteriores al 17 oct 2024;
- vigencia/suspensión/cancelación/revocación, si existieron.

### Corroboración ya disponible

El mismo permiso aparece en muestras de 2025 con:

- Benbros → Portacelis → Matamoros → patente 3830;
- Brownsville GTR → Portacelis → Nuevo Laredo → patente 3677;
- MG Energy → Portacelis → Veracruz → patente 3807.

### Qué puede resolver

Comparar la identidad de representantes y cadena logística declarada **antes/después** del cambio societario.

---

## C. SAT — Padrón de Importadores / Sector 13

### Target C1 — snapshot histórico de suspensión

- Entidad: Portacelis Gas & Oil
- RFC: `PGO240806CH8`
- Evento reportado: suspensión 1 ago 2025
- Custodio: SAT / Administración Central de Operación de Padrones
- Estado: `TARGET` para fila/documento primario histórico

### Recuperar

- lista oficial de suspendidos con corte próximo a agosto 2025;
- fila exacta de Portacelis;
- causal codificada;
- fecha efectiva;
- posteriores movimientos/reincorporación, si existieron.

### Target C2 — expediente Sector 13

Buscar, en la medida legalmente accesible:

- alta;
- aumentos/disminuciones de sector;
- socios/accionistas/representantes declarados;
- instrumentos protocolizados aportados;
- permiso SENER aportado;
- agentes aduanales autorizados;
- escritos/contratos/CFDI requeridos para acreditar operación;
- expediente de suspensión/reincorporación.

### Restricción

Parte de la información fiscal puede estar protegida por secreto fiscal. Registrar una negativa o reserva como resultado de adquisición, no como evidencia sustantiva.

---

## D. Beneficiario controlador

### Target D1

Identificar documentalmente quién fue considerado beneficiario controlador de Portacelis en los periodos:

- 6 ago–16 oct 2024;
- 17 oct 2024–1 ago 2025;
- cualquier periodo posterior relevante.

### Posibles custodios

- propia sociedad/contabilidad;
- SAT;
- notaría/protocolo según acto;
- UIF/CNBV sólo dentro de mecanismos legales no públicos;
- expedientes judiciales si la información fue incorporada y desellada.

### Regla

No inferir beneficiario controlador a partir de:

- amistad;
- parentesco de terceros;
- mismo domicilio;
- mismo contador;
- existencia de un poder aislado.

Esos datos dirigen investigación, no sustituyen el documento.

---

## E. Estados Unidos — cateo de Ikon Midstream

### Target E1 — search warrant file

- Fecha del cateo: 14 abr 2026
- Autoridad confirmada: Homeland Security Investigations
- Entidad: Ikon Midstream LLC, Houston
- Estado: orden criminal confirmada; affidavit/return/inventory `NO-LOCALIZADO` públicamente al cierre de Ola 5

### Buscar

- application for search warrant;
- affidavit in support;
- warrant;
- return/inventory;
- docket number;
- sealing/unsealing order;
- criminal complaint;
- indictment;
- exhibits;
- posteriores civil-forfeiture proceedings.

### Afirmaciones a separar

1. HSI ejecutó orden criminal → confirmado por DHS/Reuters.
2. Se buscaron computadoras/documentos → reportado por Reuters con fuente oficial.
3. MCCI afirma que fueron incautados documentos de transacciones con Portacelis → C, pendiente de inventario.
4. Portacelis era objetivo criminal de EE.UU. → **no demostrado**.

### Vías

- PACER/RECAP si aparece docket;
- DOJ/USAO Southern District of Texas;
- DHS/ICE/HSI releases;
- FOIA, reconociendo posibles exenciones por investigación activa;
- monitoreo de futuros indictments/unsealings.

---

## F. CFDI / downstream Portacelis → Oxy

### Target F1 — paquete documental de facturas

N+ afirma haber revisado facturas de Oxy Services relacionadas con diésel transportado en Pacific Tamerlane.

Recuperar, si aparecen en fuente pública/judicial:

- UUID;
- emisor;
- receptor;
- fecha;
- litros/unidad;
- precio unitario;
- impuestos;
- método/forma de pago;
- complemento de pago;
- contrato/orden de compra;
- cliente final.

### Restricción

No intentar acceder a CFDI privados mediante credenciales ajenas o mecanismos no autorizados. Sólo fuentes públicas, documentos aportados legalmente, expedientes judiciales o divulgaciones legítimas.

---

## G. Estado de adquisición al cierre de Ola 5

| Target | Estado | Valor para hipótesis |
|---|---|---|
| FME RPC Portacelis | LEAD exacto / certificación pendiente | Muy alto |
| Poder 11 oct 2024 | reportado / instrumento completo pendiente | Muy alto |
| Acta 17 oct 2024 | reportada / certificación pendiente | Muy alto |
| Permiso `1701C124002733` | uso operativo corroborado / expediente pendiente | Muy alto |
| SAT suspensión histórica | reportada / fila primaria pendiente | Alto |
| Sector 13 completo | pendiente / acceso posiblemente restringido | Muy alto |
| Beneficiario controlador | no localizado | Crítico |
| CFDI Oxy completos | reportados / no obtenidos | Alto |
| Ikon warrant affidavit/inventory | no localizado públicamente | Muy alto |

---

## H. Orden recomendado de trabajo siguiente

1. **SIGER primero:** menor ambigüedad y mayor probabilidad de obtener documento certificable.
2. **SENER segundo:** permiso exacto ya conocido y corroborado en operaciones.
3. **SAT tercero:** snapshots públicos primero; después evaluar límites de acceso al expediente.
4. **US warrant:** monitorizar desellado/docket y buscar regularmente.
5. **CFDI/downstream:** sólo si aparecen copias legítimas en investigaciones, litigios o fuentes documentales.

El objetivo no es acumular documentos: es obtener los pocos que puedan modificar simultáneamente varias aristas de alta importancia.
