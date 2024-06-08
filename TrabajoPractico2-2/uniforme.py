import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Transformada Inversa
def generar_inversa(a, b, tamanio):
    u = np.random.uniform(0, 1, tamanio)
    return a + u * (b - a)

#Método del Rechazo
def generar_rechazo(a, b, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.uniform(a,b)
        u = np.random.uniform(0,1)
        if u <= 1:
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_inversa = generar_inversa(0, 10, 10000)
valores_rechazo = generar_rechazo(0, 10, 10000)

# Visualizacion Inversa
plt.hist(valores_inversa, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.uniform(0,10,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()