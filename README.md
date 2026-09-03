# SWA — Arquitectura de Software · UTEC 2026-II

Los casos de estudio del curso, cada uno en su carpeta. Los tres primeros llegaron con la
historia completa que traían de sus repositorios separados; el cuarto nació ya aquí.

| Carpeta | Caso | Tema |
|---|---|---|
| [`LAB01-UCI-Essalud/`](LAB01-UCI-Essalud/README.md) | #1 | Sistema de gestión de UCI para EsSalud |
| [`LAB02-Lease/`](LAB02-Lease/README.md) | #2 | Lea$e — leasing de maquinaria en Perú |
| [`LAB03-SendIt/`](LAB03-SendIt/README.md) | #3 | SendIt — remesas internacionales, por el método R.E.D.A.L.E. |
| [`LAB04-RemoteSchooly/`](LAB04-RemoteSchooly/README.md) | #4 | RemoteSchooly — educación en línea para pueblos remotos, por el método R.E.D.A.L.E. |

## Cómo se armó

Cada laboratorio vivía en su propio repositorio. Las tres historias se reescribieron para
que sus rutas colgaran de la subcarpeta correspondiente y se injertaron sobre una raíz
común, de modo que la trazabilidad sobrevive al traslado:

```bash
git log -- LAB02-Lease/          # los 57 commits del caso 2, no solo el merge
git log --follow LAB03-SendIt/docs/ENTREGA.md
```

`main` es el estado entregado de los tres. El trabajo que al momento de unificar seguía en
revisión se conservó en ramas con el prefijo del lab —`lab01/eval/iteracion-12`,
`lab02/worktree-arquitectura-diagrama`, `lab03/eval-veredicto-derivado`—, junto con
`lab01/main`, `lab02/main` y `lab03/main`, que apuntan a la punta de cada historia
original. Las ramas que ya estaban contenidas en `main` no se arrastraron.

Los repositorios de origen siguen en pie y son de solo lectura desde ahora:
[SWA-LAB01-UCI-Essalud](https://github.com/LuisMUtec/SWA-LAB01-UCI-Essalud),
[SWA-LAB02-Lease](https://github.com/LuisMUtec/SWA-LAB02-Lease),
[SWA-LAB03-SendIt](https://github.com/LuisMUtec/SWA-LAB03-SendIt).

## Harness

Por ahora cada laboratorio conserva el suyo dentro de su carpeta: `.claude/` con los
agentes de persona y los skills de Spec Kit, `.specify/` con la constitución del caso, y
sus propios scripts. Spec Kit resuelve su raíz buscando el `.specify/` más cercano hacia
arriba, así que sigue funcionando desde dentro de cada lab. Unificarlos en un harness
único en la raíz es el paso siguiente, aún pendiente.
