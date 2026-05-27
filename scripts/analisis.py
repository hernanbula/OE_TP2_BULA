# Script de análisis de ventas - Escenario B
# Autor simulado: P2 - Paco

# Importar librerías necesarias
import csv          # Para leer archivos CSV (datos tabulares)
import matplotlib.pyplot as plt  # Para generar gráficos de barras

# ===========================================
# CONFIGURACIÓN DE RUTAS (relativas al repositorio)
# ===========================================
ruta_csv = "datos/sales_sample_2024.csv"      # Archivo de entrada
ruta_resumen = "resultados/resumen.txt"       # Archivo de salida (texto)
ruta_grafico = "resultados/ventas_por_mes.png" # Archivo de salida (imagen)

# ===========================================
# INICIALIZAR VARIABLES
# ===========================================
total_ventas = 0          # Acumulador de ventas totales
ventas_mes = {}           # Diccionario: clave = mes (AAAA-MM), valor = suma de ventas

# ===========================================
# PROCESAR EL ARCHIVO CSV
# ===========================================
# El CSV tiene columnas: id, fecha, importe
# Se asume que la primera fila es encabezado.

with open(ruta_csv, newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)          # Saltar la primera línea (encabezado)

    for fila in lector:
        fecha = fila[1]          # Segunda columna: fecha (ej: "2024-01-15")
        importe = float(fila[2]) # Tercera columna: importe de la venta

        total_ventas += importe

        mes = fecha[:7]          # Extraer "AAAA-MM" (ej: "2024-01")
        # Acumular ventas por mes
        if mes in ventas_mes:
            ventas_mes[mes] += importe
        else:
            ventas_mes[mes] = importe

# ===========================================
# GENERAR ARCHIVO DE RESUMEN (TEXTO)
# ===========================================
with open(ruta_resumen, "w", encoding="utf-8") as resumen:
    resumen.write(f"Ventas totales: ${total_ventas:.2f}\n\n")
    resumen.write("Ventas por mes:\n")
    for mes, monto in sorted(ventas_mes.items()):
        resumen.write(f"{mes}: ${monto:.2f}\n")
# Este archivo se guarda en la carpeta /resultados

# ===========================================
# GENERAR GRÁFICO DE BARRAS (VENTAS POR MES)
# ===========================================
meses = list(ventas_mes.keys())
montos = list(ventas_mes.values())

plt.figure(figsize=(10, 5))
plt.bar(meses, montos, color='skyblue')
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.title("Ventas por mes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(ruta_grafico)   # Guarda el gráfico en /resultados
plt.show()                  # Muestra el gráfico en pantalla (útil en Colab)

# ===========================================
# FIN DEL PROCESO
# ===========================================
print("Análisis completado.")
print(f"Resumen guardado en: {ruta_resumen}")
print(f"Gráfico guardado en: {ruta_grafico}")
