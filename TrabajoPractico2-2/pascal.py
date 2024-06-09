import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribucion Pascal
#Transformada Inversa
def generar_pascal(alpha, beta, tamanio):
    muestras = []
    for i in range(tamanio):
        x = 0
        for j in range(alpha):
            x += -np.log(np.random.uniform(0, 1))
        muestras.append(x / beta)
    return np.array(muestras)

#Método del Rechazo
def generar_pascal_rechazo(alpha, beta, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.gamma(alpha, 1/beta)
        u = np.random.uniform(0,1)
        if u <= (beta**alpha * x**(alpha-1) * np.exp(-beta*x)) / np.math.factorial(alpha-1):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_pascal = generar_pascal(5, 1, 10000)
valores_pascal_rechazo = generar_pascal_rechazo(5, 1, 10000)

# Visualizacion Inversa
plt.hist(valores_pascal, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_pascal_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.gamma(5,1,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()