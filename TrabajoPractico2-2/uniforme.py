import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import math

#Distribucion Uniforme
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

#Distribucion Gamma
#Transformada Inversa
def generar_gamma(alpha, beta, tamanio):
    muestras = []
    for i in range(tamanio):
        x = 0
        for j in range(alpha):
            x += -np.log(np.random.uniform(0, 1))
        muestras.append(x / beta)
    return np.array(muestras)

#Método del Rechazo
def generar_gamma_rechazo(alpha, beta, tamanio):
    muestras=[]
    while (len(muestras) < tamanio):
        x = np.random.gamma(alpha, 1/beta)
        u = np.random.uniform(0,1)
        if u <= (beta**alpha * x**(alpha-1) * np.exp(-beta*x)) / np.math.factorial(alpha-1):
            muestras.append(x)
    return np.array(muestras)

# Generar valores
valores_gamma = generar_gamma(5, 1, 10000)
valores_gamma_rechazo = generar_gamma_rechazo(5, 1, 10000)

# Visualizacion Inversa
plt.hist(valores_gamma, bins=50, density=True)
plt.title('Transformada Inversa')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Visualizacion Rechazo
plt.hist(valores_gamma_rechazo, bins=50, density=True)
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




