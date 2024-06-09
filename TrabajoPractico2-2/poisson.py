import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribucion Poisson
#Transformada Inversa
def generar_poisson(lam, tamanio):
    muestras = []
    for i in range(tamanio):
        x = 0
        p = 1
        while p >= np.exp(-lam):
            p *= np.random.uniform(0, 1)
            x += 1
        muestras.append(x - 1)
    return np.array(muestras)

#Método del Rechazo
def generar_poisson_rechazo(lam, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.poisson(lam)
        u = np.random.uniform(0,1)
        if u <= (lam**x * np.exp(-lam)) / np.math.factorial(x):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_poisson = generar_poisson(5, 10000)
valores_poisson_rechazo = generar_poisson_rechazo(5, 10000)

# Visualizacion Inversa
plt.hist(valores_poisson, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_poisson_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.poisson(5,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()