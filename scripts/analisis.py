# ============================================================================
# SCRIPT DE ANÁLISIS DE VENTAS - ESCENARIO B
# ============================================================================
# Autor original: P2 - Paco
# Revisión y comentarios adicionales: P3 - Luis
# Fecha de revisión: 2026-05-27
# ============================================================================
# OBJETIVO DEL SCRIPT:
#   Procesar un archivo CSV que contiene ventas diarias, calcular el total
#   vendido y las ventas acumuladas por mes, y generar:
#     1) Un archivo de texto con el resumen (resultados/resumen.txt)
#     2) Un gráfico de barras mostrando ventas por mes (resultados/ventas_por_mes.png)
# ============================================================================

# ----------------------------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------------------------------
# csv: librería estándar de Python para leer y escribir archivos CSV.
#      No necesita instalación adicional. Se usa para procesar el dataset.
import csv

# matplotlib.pyplot: librería para generar gráficos. Se utiliza para crear
#                    un gráfico de barras que visualiza las ventas por mes.
#                    Si no está instalada, se instala con: pip install matplotlib
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# CONFIGURACIÓN DE RUTAS (TODAS RELATIVAS, PARA QUE SEA REPRODUCIBLE)
# ----------------------------------------------------------------------------
# Ruta del archivo de entrada (dataset). Debe estar dentro de la carpeta /datos.
ruta_csv = "datos/sales_sample_2024.csv"

# Ruta donde se guardará el resumen en texto plano (dentro de /resultados).
ruta_resumen = "resultados/resumen.txt"

# Ruta donde se guardará el gráfico de barras (dentro de /resultados).
ruta_grafico = "resultados/ventas_por_mes.png"

# ----------------------------------------------------------------------------
# INICIALIZACIÓN DE VARIABLES
# ----------------------------------------------------------------------------
# total_ventas: acumulador simple que sumará el importe de todas las filas.
total_ventas = 0

# ventas_mes: diccionario cuyas claves son los meses (formato "AAAA-MM")
#             y los valores son la suma de ventas de ese mes.
# Ejemplo: {"2024-01": 3800, "2024-02": 4300, ...}
ventas_mes = {}

# ----------------------------------------------------------------------------
# LECTURA Y PROCESAMIENTO DEL ARCHIVO CSV
# ----------------------------------------------------------------------------
# Se asume que el archivo CSV tiene las siguientes columnas:
#   - Columna 0: id (identificador, no se usa)
#   - Columna 1: fecha (formato "AAAA-MM-DD", ej: "2024-01-15")
#   - Columna 2: importe (número decimal con punto, ej: 1500.00)
# La primera fila es un encabezado, por lo que la saltamos.

with open(ruta_csv, newline='', encoding='utf-8') as archivo:
    # Crear un lector de CSV
    lector = csv.reader(archivo)
    
    # Saltar la primera línea (cabecera)
    next(lector)
    
    # Iterar sobre cada fila del archivo
    for fila in lector:
        # Extraer los datos relevantes
        fecha = fila[1]          # Segunda columna: fecha
        importe = float(fila[2]) # Tercera columna: importe, convertido a float
        
        # Sumar al total general
        total_ventas += importe
        
        # Extraer el mes: tomamos los primeros 7 caracteres de la fecha ("AAAA-MM")
        # Ejemplo: "2024-01-15" -> "2024-01"
        mes = fecha[:7]
        
        # Acumular las ventas por mes.
        # Si el mes ya existe en el diccionario, se suma el importe;
        # si no existe, se crea la entrada con el importe actual.
        if mes in ventas_mes:
            ventas_mes[mes] += importe
        else:
            ventas_mes[mes] = importe

# ----------------------------------------------------------------------------
# GENERACIÓN DEL ARCHIVO DE RESUMEN (TEXTO)
# ----------------------------------------------------------------------------
# Se escribe un archivo plano con los resultados obtenidos.
# Se ordenan los meses cronológicamente para facilitar la lectura.

with open(ruta_resumen, "w", encoding="utf-8") as resumen:
    # Escribir el total de ventas con dos decimales
    resumen.write(f"Ventas totales: ${total_ventas:.2f}\n\n")
    
    # Escribir el detalle por mes
    resumen.write("Ventas por mes:\n")
    for mes, monto in sorted(ventas_mes.items()):
        resumen.write(f"{mes}: ${monto:.2f}\n")

# ----------------------------------------------------------------------------
# GENERACIÓN DEL GRÁFICO DE BARRAS
# ----------------------------------------------------------------------------
# Preparamos los datos para el gráfico: listas de meses y montos
meses = list(ventas_mes.keys())
montos = list(ventas_mes.values())

# Configurar el tamaño de la figura (10 pulgadas de ancho, 5 de alto)
plt.figure(figsize=(10, 5))

# Crear el gráfico de barras. El color 'skyblue' es opcional pero agradable.
plt.bar(meses, montos, color='skyblue')

# Etiquetas y título
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.title("Ventas por mes")

# Rotar las etiquetas del eje X para que no se superpongan (45 grados)
plt.xticks(rotation=45)

# Ajustar automáticamente los márgenes para que todo quede visible
plt.tight_layout()

# Guardar el gráfico como archivo PNG en la carpeta /resultados
plt.savefig(ruta_grafico)

# Mostrar el gráfico en la pantalla (útil cuando se ejecuta en Colab)
plt.show()

# ----------------------------------------------------------------------------
# FIN DEL PROCESO
# ----------------------------------------------------------------------------
print("Análisis completado.")
print(f"Resumen guardado en: {ruta_resumen}")
print(f"Gráfico guardado en: {ruta_grafico}")