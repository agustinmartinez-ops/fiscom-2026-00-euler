# Primeros pasos: Euler y tiro oblicuo

Este repositorio es una práctica breve para aprender cómo trabajaremos durante
la materia. Van a implementar un integrador de Euler, comprobarlo con tests y
comparar una trayectoria numérica con la solución exacta.

## 1. Clonar el repositorio

La cátedra les dará la URL del repositorio de su grupo:

```bash
git clone <URL-DEL-REPOSITORIO>
cd <NOMBRE-DEL-REPOSITORIO>
```

## 2. Instalar `uv`

En macOS o Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cierren y vuelvan a abrir la terminal. Comprueben la instalación con:

```bash
uv --version
```

## 3. Preparar el entorno

Desde la raíz del repositorio:

```bash
uv sync
uv run pytest
```

La primera vez, dos tests fallarán porque `integrar_euler` todavía no está
implementada. Ese es el punto de partida, no un problema de instalación.

## 4. Trabajar

1. Lean `question.md` y anoten sus predicciones **antes** de simular.
2. Completen `integrar_euler` en `src/tiro_oblicuo/simulacion.py`.
3. Corran `uv run pytest` hasta que los tests pasen.
4. Generen la figura con:

   ```bash
   uv run python experiments/trayectoria.py
   ```

5. Abran `results/trayectoria.png` y completen `lab.md`.
6. Si usaron IA, documenten en `ai-use.md` qué delegaron y cómo lo verificaron.

## Estructura

```text
README.md                           instalación y recorrido
question.md                         predicciones previas
src/tiro_oblicuo/simulacion.py      modelo, Euler y solución exacta
tests/test_simulacion.py            controles físicos y numéricos
experiments/trayectoria.py          genera la figura
results/                             resultados regenerables
lab.md                               afirmación, evidencia y limitaciones
ai-use.md                            uso y verificación de IA
pyproject.toml                       Python y dependencias
```
