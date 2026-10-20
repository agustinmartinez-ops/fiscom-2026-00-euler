import numpy as np

from tiro_oblicuo.simulacion import derivada, integrar_euler, solucion_exacta


def test_newton_da_aceleracion_vertical() -> None:
    """Sin rozamiento, Newton exige ax = 0 y ay = -g."""

    cambio = derivada(np.array([2.0, 3.0, 4.0, 5.0]), gravedad=10.0)
    np.testing.assert_allclose(cambio, [4.0, 5.0, 0.0, -10.0])


def test_euler_hace_un_paso_explicito() -> None:
    """Un paso debe usar sólo la derivada al comienzo del intervalo."""

    inicial = np.array([0.0, 0.0, 3.0, 4.0])
    tiempos, estados = integrar_euler(inicial, dt=0.1, pasos=1, gravedad=10.0)
    np.testing.assert_allclose(tiempos, [0.0, 0.1])
    np.testing.assert_allclose(estados, [inicial, [0.3, 0.4, 3.0, 3.0]])


def test_reducir_dt_reduce_el_error_de_posicion() -> None:
    """Euler debe converger a la trayectoria exacta al reducir el paso."""

    inicial = np.array([0.0, 0.0, 8.0, 12.0])
    errores = []
    for dt in (0.1, 0.05):
        tiempos, estados = integrar_euler(inicial, dt=dt, pasos=round(1.0 / dt))
        exacta = solucion_exacta(tiempos, inicial)
        errores.append(np.max(np.abs(estados[:, :2] - exacta[:, :2])))

    assert errores[1] < errores[0]
    assert np.isclose(errores[0] / errores[1], 2.0, rtol=0.05)
