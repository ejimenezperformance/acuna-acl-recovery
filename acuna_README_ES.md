# Recuperación de LCA de Acuña — Velocidad Cruda vs. Eficiencia en Bases Robadas

**Ronald Acuña Jr. se desgarró el LCA dos veces — rodilla derecha (julio
2021), rodilla izquierda (mayo 2024) — dando una trayectoria poco común
de tres puntos en la recuperación de un mismo atleta de élite. La
velocidad de sprint declinó en dos pasos claros, uno después de cada
cirugía, y sigue cayendo en 2026. El éxito en bases robadas no sigue el
mismo patrón — alcanzó su mejor marca de carrera (90%) el año después
de su segunda cirugía, y luego cayó fuerte esta temporada.**

Parte del portafolio analítico de [Emerson Performance](https://github.com/ejimenezperformance) (marco EP-TSP). Este es el espejo de tren inferior de `tj-recovery-trajectory` — la misma pregunta de retorno al juego, aplicada a una lesión de rodilla en vez de codo, y a corrido de bases en vez de pitcheo.

*[English version available here](https://github.com/ejimenezperformance/acuna-acl-recovery/blob/main/README.md)*

---

## Hallazgo 1 — Velocidad de sprint: alcanzó su pico antes de cualquier lesión, luego declinó en dos pasos

![Trayectoria de velocidad de sprint](https://github.com/ejimenezperformance/acuna-acl-recovery/raw/main/outputs/acuna_trajectory_ES.png)

| Temporada                    | Velocidad de Sprint (ft/s) |
| ----------------------------- | --------------------------- |
| 2018 (pico)                   | 29.6                        |
| 2019                          | 29.3                        |
| 2020                          | 29.1                        |
| 2021 (1er desgarro de LCA, jul) | 29.4                       |
| 2022                          | 28.5                        |
| 2023 (temporada 40-70)        | 28.0                        |
| 2024 (2do desgarro de LCA, may) | 27.7                       |
| 2025                          | 27.9                        |
| 2026                          | 27.2                        |

La velocidad de sprint de Acuña alcanzó su pico en 2018 (29.6 ft/s,
"plus-plus" según los estándares de Statcast) y se mantuvo de élite
hasta justo su primer desgarro de LCA — su marca de 2021 (29.4 ft/s),
el año de esa lesión, es la segunda más alta de su carrera. La caída se
da en dos pasos claros después de cada cirugía: baja a una meseta de
28.0–28.5 tras el primer desgarro, y luego baja otra vez a un rango de
27.2–27.9 tras el segundo. 2026 (27.2 ft/s) es su marca más baja hasta
ahora y no muestra señales de estabilizarse.

## Hallazgo 2 — El éxito en bases robadas cuenta una historia muy distinta

![Tasa de éxito en bases robadas](https://github.com/ejimenezperformance/acuna-acl-recovery/raw/main/outputs/acuna_sb_success_ES.png)

| Temporada                   | BR | AT | Tasa de Éxito |
| ---------------------------- | --- | --- | -------------- |
| 2021 (1er desgarro)          | 17 | 6  | 73.9%          |
| 2022                         | 29 | 11 | 72.5%          |
| 2023                         | 73 | 14 | 83.9%          |
| 2024 (2do desgarro)          | 16 | 3  | 84.2%          |
| **2025 (tras 2da cirugía)**  | 9  | 1  | **90.0%**      |
| 2026                         | 16 | 7  | 69.6%          |

A diferencia de la velocidad de sprint, la eficiencia en bases robadas
no siguió una simple caída post-lesión. Su mejor tasa de éxito de
carrera (90.0%) llegó la temporada *después* de su segunda cirugía de
LCA — su temporada de menor velocidad registrada — no antes. Este año
(2026) muestra su caída más pronunciada en una sola temporada desde sus
años de novato.

**Verificación estadística:** una prueba z de dos proporciones
comparando 2026 (16/23, 69.6%) contra su tasa de carrera combinada
2018-2025 (205/255, 80.4%) no es estadísticamente significativa
(z=-1.232, p=0.218). Con solo 23 intentos en 2026, la caída de este año
— aunque visualmente la más pronunciada en el gráfico — no se puede
distinguir con confianza de la variación normal de temporada a
temporada. Vale la pena seguirla conforme avance la temporada, todavía
no es un patrón confirmado.

*Nota: los conteos de BR/AT de 2026 en la tabla reflejan el momento en
que se extrajo este análisis (aproximadamente a mitad de temporada) —
revisa Baseball-Reference para el total actual antes de citar este
número como final.*

## Hallazgo 3 — 2026: el lead más largo de su carrera, el mismo año que cayó el éxito

![Distancia de lead](https://github.com/ejimenezperformance/acuna-acl-recovery/raw/main/outputs/acuna_lead_distance_ES.png)

| Temporada | Distancia de Lead en Intentos de BR (ft) | % de Intento de Robo |
| --------- | ----------------------------------------- | --------------------- |
| 2020      | 11.0                                       | 2.0%                   |
| 2023      | 12.3                                       | 4.9%                   |
| 2025      | 12.1                                       | 0.8%                   |
| **2026**  | **13.6**                                   | 3.7%                   |

Su distancia de lead secundario en intentos de base robada se ha
mantenido generalmente en una banda estrecha de 11.0–12.3 ft en la
mayoría de temporadas — hasta 2026, donde el promedio de temporada
salta a un máximo de carrera de 13.6 ft.

**Verificación estadística:** usando datos verificados por intento (no
solo el promedio de temporada), una prueba t comparando 2026 (n=19
intentos, media 13.28 ft, DE 5.57) contra 2023 (n=68 intentos, media
12.18 ft, DE 3.52) no es estadísticamente significativa (t=0.813,
p=0.425). La varianza mucho más alta y la muestra más pequeña de 2026
significan que el salto visualmente llamativo de este año no se puede
distinguir con confianza de la variación normal entre intentos — una
verificación real y útil, no una limitación de los datos.

## Por qué esto importa

Este es el mismo patrón de "herramienta cruda vs. eficiencia" que este
portafolio ha encontrado repetidamente del lado del bateo y el pitcheo
(`ep-swing-intelligence`, `vaa-approach-angle-study`) — pero aquí se da
dentro de la recuperación de un mismo atleta, de la misma lesión, dos
veces. La herramienta física cruda (velocidad de sprint) se degrada de
forma escalonada y rastreable que sigue de cerca la línea de tiempo de
las lesiones. La capa de habilidad/decisión construida sobre esa
herramienta (éxito en bases robadas — leer al pitcher, timing del salto,
juicio situacional) no se degrada en el mismo calendario, y en este caso
parece haberse mantenido *intacta o incluso afinada* en el año
inmediatamente posterior a la cirugía más reciente. Para un cuerpo
técnico, esto argumenta en contra de asumir que un corredor más lento es
automáticamente peor robando bases — son dos habilidades relacionadas
pero distintas, con calendarios de recuperación diferentes.

## Estructura del repo

```
acuna-acl-recovery/
|-- data/
|   |-- sprint_speed_by_year/
|   |-- acuna_sprint_speed_trajectory.csv
|   `-- acuna_sb_success_rate.csv
|-- scripts/
|   |-- acuna_analysis.py
|   `-- ep_chart_style.py
`-- outputs/
    |-- acuna_trajectory_{EN,ES}.png
    |-- acuna_sb_success_{EN,ES}.png
    `-- acuna_lead_distance_{EN,ES}.png
```

## Reproducir el análisis

```
git clone https://github.com/ejimenezperformance/acuna-acl-recovery.git
cd acuna-acl-recovery
pip install pandas matplotlib
python scripts/acuna_analysis.py
```

## Metodología

- **Fechas de lesión:** 10 de julio de 2021 (rotura de LCA derecho) y 26
  de mayo de 2024 (rotura de LCA izquierdo, cirugía el 6 de junio de
  2024) — algunos artículos deportivos retrospectivos reportan el 20 de
  julio de 2021 para la primera lesión; esto parece ser un error
  copiado, ya que reportes del mismo día por MLB.com y Sports
  Illustrated, ambos fechados 10 de julio de 2021, confirman la fecha
  correcta.
- **Velocidad de sprint:** Tabla de líderes de Sprint Speed de Baseball
  Savant, extraída por temporada, 2018-2026. Cruzada directamente contra
  la tabla de Statcast Running Statistics de la página del jugador en
  Baseball Savant.
- **Datos de bases robadas:** Página oficial de estadísticas de carrera
  de Baseball-Reference, confirmada de forma independiente contra su
  propia columna SB% (calculada como SB/(SB+CS)) para consistencia
  interna.
- **Datos de distancia de lead:** Desglose de robo de bases de Statcast
  de Baseball Savant, 2018-2026.

## Limitaciones

- **El Hallazgo 3 (distancia de lead) originalmente no tenía datos por
  intento para una prueba de significancia.** Esto se resolvió:
  registros individuales de intentos de base robada (con distancia de
  lead por intento) se obtuvieron directamente del desglose de robo de
  bases específico del jugador en Baseball Savant, tanto para 2023 como
  2026, transcritos manualmente y verificados contra las cifras
  oficiales de promedio de temporada (2023: media calculada 12.18 ft
  vs. oficial 12.3 ft; 2026: media calculada 13.28 ft vs. oficial 13.6
  ft; ambas dentro de la tolerancia de redondeo esperada, y los conteos
  de bases robadas coincidieron con los totales oficiales). Esto da
  confianza de que la transcripción es precisa.

- **Este es un estudio de caso de un solo jugador**, no un patrón
  multi-jugador — demuestra lo que pasó con un atleta, no una
  afirmación generalizable sobre la recuperación de LCA en jugadores de
  posición. Está intencionalmente delimitado así dada la rareza de una
  trayectoria de dos lesiones limpia y bien documentada para un mismo
  jugador (ver `tj-recovery-trajectory` para la versión multi-pitcher de
  esta misma pregunta aplicada a cirugía de codo).

- **2026 es una temporada parcial.** La caída pronunciada en la tasa de
  éxito de BR este año podría reflejar parcialmente una muestra más
  pequeña de intentos (23) comparada con temporadas completas
  anteriores, y tanto las cifras de velocidad de sprint como las de BR
  reflejan el punto de la temporada en que se extrajo este análisis —
  actualízalas contra Baseball Savant / Baseball-Reference antes de
  citarlas como número final de temporada.

- **No se prueba ningún mecanismo** de por qué el éxito en bases
  robadas no cayó junto con la velocidad — posibles explicaciones
  (mejores lecturas de salto, selectividad reducida de intentos,
  factores específicos de catcher/pitcher) no se distinguen aquí.

- **Ambas lesiones afectaron rodillas distintas** — este análisis no
  prueba si la rodilla específica (pierna dominante de impulso vs.
  pierna de plantación) afectó la recuperación de forma diferente.

## Contacto

**Emerson Jiménez** — Entrenador de Fuerza y Acondicionamiento,
Especialista en Rendimiento de Béisbol. [Emerson Performance](https://github.com/ejimenezperformance) · [@emersonperformance](https://instagram.com/emersonperformance)

---

*Marco y diseño EP-TSP © Emerson Performance. Datos de Statcast/Baseball
Savant y Baseball-Reference usados para análisis no comercial.*
