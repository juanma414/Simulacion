import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribucion Exponencial
#Transformada Inversa
def generar_exponencial(lam, tamanio):
    u = np.random.uniform(0, 1, tamanio)
    return -np.log(1 - u) / lam

#Método del Rechazo
def generar_exponencial_rechazo(lam, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.exponential(1/lam)
        u = np.random.uniform(0,1)
        if u <= lam * np.exp(-lam * x):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_exponencial = generar_exponencial(1, 10000)
valores_exponencial_rechazo = generar_exponencial_rechazo(1, 10000)

# Visualizacion Inversa
plt.hist(valores_exponencial, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_exponencial_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.exponential(1,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()