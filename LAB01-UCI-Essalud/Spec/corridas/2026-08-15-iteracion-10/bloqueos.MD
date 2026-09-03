# Bloqueos — corrida 2026-08-15-iteracion-10

Lo que esta corrida no pudo corregir porque la corrección cae fuera de los archivos que
`Spec/corridas/_ESQUEMA.MD` §«Qué puede tocar una corrida» le permite modificar.

## B1 — C1 compara el README contra la corrida equivocada por un artefacto de ordenamiento

**Qué ocurre.** `scripts/verificar-puntaje.sh` identifica la última corrida con
`find Spec/corridas -name corrida.json | sort | tail -1`, es decir, por orden lexicográfico del nombre
del directorio. Con la etiqueta `iteracion-10`, ese orden deja de coincidir con el cronológico:

```
Spec/corridas/2026-08-15-iteracion-10/corrida.json   ← esta corrida
Spec/corridas/2026-08-15-iteracion-5/corrida.json
...
Spec/corridas/2026-08-15-iteracion-9/corrida.json    ← lo que tail -1 devuelve
```

`"10" < "5"` como texto, de modo que el control toma `2026-08-15-iteracion-9` como la última corrida,
lee su `resultado.global` de 80,9 y lo compara contra el porcentaje que `README.md` publica. Esta
corrida cerró en 77,4 y publicó 77,4, así que el control reporta:

```
README.md: publica 77.4 % y la última corrida cerró en 80.9 %
```

**Por qué no se corrige.** Las tres correcciones posibles caen todas fuera de lo que una corrida puede
tocar, o convierten la vara en algo que se ajusta al número:

1. **Cambiar el criterio de «última corrida» del script** —ordenar por el campo `fecha` de cada
   `corrida.json`, o por tiempo de modificación, en vez de por nombre de directorio— es lo correcto,
   pero `scripts/*` es de solo lectura durante la corrida, y `Spec/Eval-Spec.MD` es explícita:
   «Si C1 contradice un número tuyo, el equivocado es el número. Corregir la fórmula, el techo o el
   umbral para que la discrepancia desaparezca es ajustar la vara».
2. **Renombrar el directorio de la corrida** a una etiqueta que ordene bien (`iteracion-010`) cambia
   el identificador que la corrida declara y rompería la correspondencia con `HISTORIAL.MD` y con la
   cabecera de reproducibilidad.
3. **Devolver el README a 80,9 %** haría el control verde publicando el porcentaje de una corrida
   superseded. Es exactamente el defecto que esa comprobación existe para atrapar —«Si se queda en el
   de una corrida anterior, publica un número que ya nadie sostiene»—, de modo que satisfacer la
   implementación exigiría violar la intención. No se hace.

**Qué se hizo en su lugar.** `README.md` publica 77,4 %, que es el resultado que esta corrida
sostiene; `corrida.json` declara `controles_pasan: false`, porque los nueve controles no devuelven
vacío; y la condición 5 del veredicto se declara incumplida. El veredicto de la corrida es **FAILED**
con o sin este bloqueo: las condiciones 1, 2 y 3 ya no se cumplen —global 77,4 < 80,0, D1 54,0 < 80,0
y la persona más baja 4,4 < 7,0—, de modo que este bloqueo no altera el resultado, solo la cuenta de
controles en verde.

**Qué hace falta.** Un cambio en `scripts/verificar-puntaje.sh`, en su propia rama y con su propia
revisión, que determine la última corrida por el campo `fecha` de `corrida.json` y, a igualdad de
fecha, por orden natural de la etiqueta. Hasta entonces, toda corrida cuya etiqueta lleve un número de
dos cifras reproducirá este falso positivo.
