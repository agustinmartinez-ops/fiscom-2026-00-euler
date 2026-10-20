"""Compara Euler con la solución exacta y genera results/trayectoria.png.

Ejecutar desde la raíz del repositorio con:

    uv run python experiments/trayectoria.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from tiro_oblicuo.simulacion import integrar_euler, solucion_exacta

RESULTADOS = Path(__file__).resolve().parents[1] / "results"


def main() -> None:
    rapidez = 20.0
    angulo = np.deg2rad(45.0)
    gravedad = 9.81
    dt = 0.1
    inicial = np.array([0.0, 0.0, rapidez * np.cos(angulo), rapidez * np.sin(angulo)])
    tiempo_de_vuelo = 2 * inicial[3] / gravedad
    pasos = round(tiempo_de_vuelo / dt)

    tiempos, estados = integrar_euler(inicial, dt, pasos, gravedad)
    exacta = solucion_exacta(tiempos, inicial, gravedad)
    error = np.max(np.abs(estados[:, :2] - exacta[:, :2]))

    figura, eje = plt.subplots(figsize=(6, 4))
    eje.plot(exacta[:, 0], exacta[:, 1], label="solución exacta")
    eje.plot(estados[:, 0], estados[:, 1], "o-", ms=3, label=f"Euler, dt={dt} s")
    eje.axhline(0, color="black", lw=0.8)
    eje.set(xlabel="x [m]", ylabel="y [m]", title="Tiro oblicuo sin rozamiento")
    eje.legend()

    RESULTADOS.mkdir(exist_ok=True)
    destino = RESULTADOS / "trayectoria.png"
    figura.savefig(destino, dpi=150, bbox_inches="tight")
    print(f"error máximo de posición: {error:.3f} m")
    print(f"figura: {destino}")


if __name__ == "__main__":
    main()
