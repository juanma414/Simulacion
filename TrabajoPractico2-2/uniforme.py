import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribución uniforme
def generar_uniforme(a, b, size=1):
    u = np.random.uniform(0, 1, size)
    print (u)
    print (u*b)
    return a + u * (b - a)

# Generar valores
valores_uniformes = generar_uniforme(0, 10, 10000)

# Visualización
plt.hist(valores_uniformes, bins=50, density=True)
plt.title('Histograma de valores uniformemente distribuidos')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()