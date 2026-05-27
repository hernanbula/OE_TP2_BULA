# TP2 - Organización Empresarial - Análisis de Ventas

**Estudiante:** Hernán Bula  
**Rol simulado:** P1, P2 y P3 (trabajo individual)  
**Escenario elegido:** B - Análisis de Ventas de una Pequeña Empresa  

## Descripción del proyecto

Este proyecto procesa un archivo CSV con datos de ventas diarias. Calcula el total vendido, las ventas acumuladas por mes y genera un gráfico de barras. El código está escrito en Python y se puede ejecutar en cualquier equipo con los requisitos básicos.

## Dataset utilizado

El archivo `datos/sales_sample_2024.csv` tiene tres columnas:

- id: identificador de la venta
- fecha: fecha en formato AAAA-MM-DD
- importe: monto de la venta (número decimal)

El dataset lo descargué de la fuente que recomendó la cátedra y lo guardé dentro de la carpeta `/datos`.

## Estructura del repositorio

- `/datos` → el archivo CSV original
- `/scripts` → el script `analisis.py` con todo el procesamiento
- `/resultados` → los archivos que genera el script: `resumen.txt` y `ventas_por_mes.png`
- `README.md` → este archivo
- `.gitignore` → para ignorar archivos temporales (como `__pycache__`)

## Requisitos para ejecutar el script

- Python 3 (cualquier versión moderna)
- La librería `matplotlib` (la usé para hacer el gráfico)

No hace falta instalar nada más.

## Qué hace el script cuando lo ejecuto

Al correr `python scripts/analisis.py` pasan dos cosas:

- Se crea (o sobreescribe) el archivo `resultados/resumen.txt`, que muestra las ventas totales y cuánto se vendió cada mes.
- Se genera `resultados/ventas_por_mes.png`, un gráfico de barras que ayuda a ver la evolución mes a mes.

## Revisión técnica (simulando el rol de Luis)

Como parte de la revisión por pares, me fijé en estos puntos:

- El script encuentra el CSV sin problemas porque usa una ruta relativa (`datos/...`).
- Revisé los cálculos con unos pocos registros a mano y coinciden.
- El gráfico se genera bien y se ve claro.
- No hay tokens ni contraseñas en el repositorio.
- Agregué comentarios en el script para que se entienda cada paso.

## Observaciones finales

Este trabajo práctico lo hice yo solo, pero simulé tres roles (Hugo, Paco y Luis) para cumplir con la consigna. Usé Git y GitHub para el control de versiones, y en cada commit puse el ID de la tarea de Jira correspondiente (PROY-1, PROY-2, PROY-3). Así queda todo trazado.
