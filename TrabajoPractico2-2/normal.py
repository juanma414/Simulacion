import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribucion Normal
#Transformada Inversa
def generar_normal(tamanio):
    u1 = np.random.uniform(0, 1, tamanio)
    u2 = np.random.uniform(0, 1, tamanio)
    return np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)

#Método del Rechazo
def generar_normal_rechazo(tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.normal(0,1)
        u = np.random.uniform(0,1)
        if u <= np.exp(-x**2/2) / np.sqrt(2 * np.pi):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_normal = generar_normal(10000)
valores_normal_rechazo = generar_normal_rechazo(10000)

# Visualizacion Inversa
plt.hist(valores_normal, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_normal_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.normal(0,1,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()