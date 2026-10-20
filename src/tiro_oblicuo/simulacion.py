"""Modelo de tiro oblicuo e integración con Euler explícito.

El estado se representa como ``[x, y, vx, vy]``.
"""

import numpy as np


def derivada(estado: np.ndarray, gravedad: float = 9.81) -> np.ndarray:
    """Devuelve la derivada temporal de ``[x, y, vx, vy]``."""

    x, y, vx, vy = estado
    return np.array([vx, vy, 0.0, -gravedad], dtype=float)


def integrar_euler(
    estado_inicial: np.ndarray,
    dt: float,
    pasos: int,
    gravedad: float = 9.81,
) -> tuple[np.ndarray, np.ndarray]:
    """Integra el movimiento durante ``pasos`` intervalos de tamaño ``dt``.

    Devuelve un arreglo de tiempos y otro de estados. Ambos incluyen la
    condición inicial, por lo que tienen ``pasos + 1`` elementos.
    """

    t = []
    estados = []

    for i in range(pasos + 1):
        t.append(i * dt)
        if i == 0:
            estados.append(np.asarray(estado_inicial, dtype=float))
        else:
            x0, y0, vx0, vy0 = estados[i - 1]

            estados.append([x0 + vx0 * dt, y0 + vy0 * dt, vx0, vy0 - gravedad * dt])

    return [np.asarray(t), np.asarray(estados)]


def solucion_exacta(
    tiempos: np.ndarray,
    estado_inicial: np.ndarray,
    gravedad: float = 9.81,
) -> np.ndarray:
    """Evalúa la solución analítica sin rozamiento en ``tiempos``."""

    x0, y0, vx0, vy0 = np.asarray(estado_inicial, dtype=float)
    t = np.asarray(tiempos, dtype=float)
    return np.column_stack(
        (
            x0 + vx0 * t,
            y0 + vy0 * t - 0.5 * gravedad * t**2,
            np.full_like(t, vx0),
            vy0 - gravedad * t,
        )
    )
