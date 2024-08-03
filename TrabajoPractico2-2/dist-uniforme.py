import numpy as np
import matplotlib.pyplot as plt

def generar_normal(mu, sigma, size=1):
    u1 = np.random.uniform(0, 1, size)
    u2 = np.random.uniform(0, 1, size)
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    return mu + z0 * sigma

# Ejemplo de uso
valores_normales = generar_normal(0, 1, 100000)

# Visualización
plt.hist(valores_normales, bins=300, density=True)
plt.title('Histograma de valores distribuidos normalmente')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()