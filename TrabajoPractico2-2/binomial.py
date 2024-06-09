import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import math

#Distribucion Binomial
#Transformada Inversa
def generar_binomial(n, p, tamanio):
    muestras = []
    for i in range(tamanio):
        x = 0
        for j in range(n):
            if np.random.uniform(0, 1) < p:
                x += 1
        muestras.append(x)
    return np.array(muestras)

#Método del Rechazo
def generar_binomial_rechazo(n, p, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.binomial(n, p)
        u = np.random.uniform(0,1)
        if u <= (math.factorial(n) / (math.factorial(x) * math.factorial(n-x))) * (p**x) * ((1-p)**(n-x)):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_binomial = generar_binomial(10, 0.5, 10000)
valores_binomial_rechazo = generar_binomial_rechazo(10, 0.5, 10000)

# Visualizacion Inversa
plt.hist(valores_binomial, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_binomial_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.binomial(10,0.5,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()