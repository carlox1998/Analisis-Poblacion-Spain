from pathlib import Path
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

#Usamos el path para ubicarnos en la carpeta origen o raiz, usamos el parent para volver una ruta anterior.
raiz = Path(__file__).parent.parent

#Accedemos a nuestro archivo desde la ruta.
archivo = raiz / "datos" / "población_extrangera_españa.xlsx"

#Leer el archivo excell
df = pd.read_excel(archivo, header=None)

#Creacion de la matriz usando los datos de la Fila 8 y 10, y las columnas desde la B hasta la Z del excell
matriz = np.array([
    df.iloc[7,1:26],
    df.iloc[9,1:26]    
], dtype = int)

#Imprimimos nuestra matriz en el terminal para ver que los datos son correctos
print(matriz)

#Imprimimos el tamaño de nuestra matriz en el terminal
print(f"Dimensiones: {matriz.shape}")

#Guardamos los datos en Variables
anios = matriz[0]
poblacion = matriz[1]

print("\n========== 1. GRAFICO DE LINEAS ==========")

#Tamaño del Grafico
plt.figure(figsize=(9, 6))

#Marcador circular para los años
plt.plot(anios, poblacion, marker="o", linestyle="-", label="Población Extranjera")

# Titulo y etiquetas de los ejes
plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Numero de Personas")

# Mostrar todos los años en el eje X y girar las etiquetas 45 grados
plt.xticks(anios, rotation=45)

#Hacer la cuadricula Grid
plt.grid(True, linestyle='--')

#Leyenda de la Grafica
plt.legend()

# Ajustar los margenes para que no se corten las etiquetas del eje X
plt.tight_layout()

#Mostrar la Grafica
plt.show()