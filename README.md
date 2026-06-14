# afds — Analizador de sintaxis (AFDs)

Proyecto de análisis de sintaxis basado en autómatas finitos deterministas (AFD).

`afds.py` define varios AFDs para reconocer tokens del lenguaje:

- `afd_id` — identificadores (letra o `_`, seguido de letras, dígitos o `_`)
- `afd_boolval` — valores booleanos (`true` / `false`)
- `afd_assign` — operador de asignación (`=`)
- `afd_unlogop` — operador lógico unario (`!`)
- `afd_semicol` — punto y coma (`;`)

## Uso

```bash
python afds.py
```

## Colaboradores

Trabajo en equipo. Para subir cambios:

```bash
git pull            # traer los últimos cambios antes de empezar
# ...editar...
git add .
git commit -m "describí tu cambio"
git push
```
