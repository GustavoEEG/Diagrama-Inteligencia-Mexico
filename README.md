# Diagrama Inteligencia México

Repositorio vivo para construir y versionar un **Intelligence Link Analysis** sobre actores, empresas, instituciones, eventos, proyectos, anomalías e hipótesis relacionadas con México.

## Estado inicial

**Ola 0 + Ola 1** · corte semilla: **18 de agosto de 2026**.

El tablero inicial contiene:

- 35 nodos;
- 47 relaciones;
- 24 fuentes registradas;
- 5 hipótesis de trabajo;
- escala epistemológica A–G;
- cronología semilla 2018–2026.

## Estructura

```text
index.html
├── data/
│   ├── nodes.json
│   ├── edges.json
│   ├── sources.json
│   ├── hypotheses.json
│   └── timeline.json
└── docs/
    └── methodology.md
```

`index.html` es el motor visual. El conocimiento se mantiene separado en JSON para que cada ola pueda ampliar o corregir el universo mediante pull requests pequeños y trazables.

## Principio central

**Una ruta entre nodos no demuestra culpabilidad, conocimiento, intención ni coordinación entre sus extremos.**

Las relaciones A–B forman el núcleo factual/documentado. C corresponde a información reportada o alegada. D–G contienen inferencias, hipótesis y wildcards que deben permanecer visual y metodológicamente separadas de los hechos.

Consulta [`docs/methodology.md`](docs/methodology.md) antes de añadir o cambiar una arista.

## Flujo de investigación

```text
investigación → fuentes → nodos → aristas → contradicciones → hipótesis → red team → PR → revisión → merge
```

Cada ola debe preferir una rama temática, por ejemplo:

- `agent/wave-02-amilcar-olan`
- `agent/wave-03-portacelis-ikon`
- `agent/wave-04-customs-navy`
- `agent/red-team-h01`

## Visualización

El tablero carga los archivos `data/*.json` por HTTP. Para desarrollo puede servirse con cualquier servidor estático; para publicación, el repo está preparado para usar GitHub Pages desde la raíz de la rama principal una vez que se habilite.
