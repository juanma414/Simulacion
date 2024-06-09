import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

#Distribucion Hipergeometrica
#Transformada Inversa
def generar_hipergeometrica(N, M, n, tamanio):
    muestras = []
    for i in range(tamanio):
        x = 0
        for j in range(n):
            if N == 0:  # Verificar si N es cero
                break  # Si es así, salir del bucle
            if np.random.uniform(0, 1) < M / N:
                x += 1
                M -= 1
            N -= 1
        muestras.append(x)
    return np.array(muestras)

#Método del Rechazo
def generar_hipergeometrica_rechazo(N, M, n, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.hypergeometric(N, M, n)
        u = np.random.uniform(0,1)
        if u <= (np.math.factorial(M) / (np.math.factorial(x) * np.math.factorial(M-x))) * (np.math.factorial(N-M) / (np.math.factorial(n-x) * np.math.factorial(N-M-n+x))) / (np.math.factorial(N) / (np.math.factorial(n) * np.math.factorial(N-n))):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_hipergeometrica = generar_hipergeometrica(100, 50, 10, 10000)
valores_hipergeometrica_rechazo = generar_hipergeometrica_rechazo(100, 50, 10, 10000)

# Visualizacion Inversa
plt.hist(valores_hipergeometrica, bins=50, density=True)
plt.title('HG Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_hipergeometrica_rechazo, bins=50, density=True)
plt.title('Metodo del Rechazo')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Python
plt.hist((np.random.hypergeometric(100,50,10,10000)), bins=50, density=True)
plt.title('Generado por Python')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()