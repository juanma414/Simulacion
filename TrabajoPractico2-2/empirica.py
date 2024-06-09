import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribucion Empirica Discreta
def generar_empirica_discreta(valores, probabilidades, tamanio):
    acumulada = np.cumsum(probabilidades)
    indices = np.digitize(np.random.uniform(0, 1, tamanio), acumulada)
    return [valores[i-1] for i in indices]

# Generar valores
valores_empirica_discreta = generar_empirica_discreta([1, 2, 3, 4], [0.1, 0.2, 0.3, 0.4], 10000)
valores_empirica_discreta_rechazo = generar_empirica_discreta([1, 2, 3, 4], [0.1, 0.2, 0.3, 0.4], 10000)

# Visualizacion Inversa 
plt.hist(valores_empirica_discreta, bins=50, density=True)
plt.title('ED Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_empirica_discreta_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.choice([1, 2, 3, 4], 10000, p=[0.1, 0.2, 0.3, 0.4])), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()