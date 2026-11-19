from pathlib import Path
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

raiz = Path(__file__).parent.parent
archivo = raiz / "datos" / "población_extrangera_españa.xlsx"

df = pd.read_excel(archivo, header=None)

matriz = np.array([
    df.iloc[7,1:26],
    df.iloc[9,1:26]    
], dtype = int)



print(matriz)

print(f"Dimensiones: {matriz.shape}")

anios = matriz[0]
poblacion = matriz[1]

print("\n========== 1. GRAFICO DE LINEAS ==========")
#Tamaño del Grafico
plt.figure(figsize=(9, 6))

#Marcador circular para los años
plt.plot(anios, poblacion, marker="o", linestyle="-", label="Población Extranjera")
plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Numero de Personas")
plt.xticks(anios, rotation=45)
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()