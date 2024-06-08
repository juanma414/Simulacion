import matplotlib.pyplot as plt  # type: ignore
import random
import pandas as pd   # type: ignore
import scipy   # type: ignore
import numpy as np   # type: ignore
from scipy.stats import chisquare, kstest , pearsonr  # type: ignore

#region LCG
#GENERADOR LCG
class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def next_in_range(self, min_val, max_val):
        return min_val + (self.next() % (max_val - min_val + 1))

# Crear una instancia del LCG
lcg = LCG(seed=1)

# Generar una lista de números aleatorios con el Método LCG
lista_lcg = [lcg.next_in_range(1, 100) for _ in range(100000)]


# Crear un gráfico de dispersión de los números generados por LCG
plt.figure(figsize=(10, 6))
plt.scatter(range(len(lista_lcg)), lista_lcg, s=1)
plt.title('Números Generados por el LCG')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()


# endregion

#region METODO DE LOS CUADRADOS 
class MiddleSquare:
    def __init__(self, seed, n_digits):
        self.seed = seed
        self.n_digits = n_digits
        self.max_value = 10 ** n_digits
    
    def next(self):
        # Elevar la semilla al cuadrado
        squared = str(self.seed ** 2).zfill(2 * self.n_digits)
        # Extraer la parte media
        start = (len(squared) - self.n_digits) // 2
        end = start + self.n_digits
        new_seed_str = squared[start:end]
        # Actualizar la semilla
        self.seed = int(new_seed_str)
        return self.seed
    
    def next_in_range(self, min_val, max_val):
        # Generar el siguiente número en el rango especificado
        return min_val + (self.next() % (max_val - min_val + 1))

# Crear una instancia del generador
seed = 15349803495615  # Semilla inicial 
n_digits = 14  # Número de dígitos de la semilla
ms = MiddleSquare(seed, n_digits)
lista_cuadrados = ms.next()

# Generar una lista de números aleatorios con el Método de los Cuadrados
lista_cuadrados = [ms.next_in_range(1, 100) for _ in range(100000)]

# Crear un gráfico de dispersión de los números generados por MS
plt.figure(figsize=(10, 6))
plt.scatter(range(len(lista_cuadrados)), lista_cuadrados, s=1)
plt.title('Números Generados por el Método de la Parte Media del Cuadrado')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()
#endregion

#region METODO RANDOM DE PYTHON

# Generar una lista de números aleatorios con el método por defecto de Python
lista_python = [random.randint(1, 100) for _ in range(100000)]

# Crear un gráfico de dispersión de los números generados por Python
plt.figure(figsize=(10, 6))
plt.scatter(range(len(lista_python)), lista_python, s=1)
plt.title('Números Generados por random de Python')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()
#endregion

#region TESTS PARA LCG
 
 #TESTS PARA VERIFICACION DE GENERADORES

# Prueba de frecuencia (Chi-cuadrado)
# Definir los intervalos (bins)
observed_freq, _ = np.histogram(lista_lcg, bins=range(1, 102))  # 100 bins de tamaño 1 (1-100)
expected_freq = np.full_like(observed_freq, len(lista_lcg) / 100)

# Realizar la prueba de chi-cuadrado
chi2_stat, p_val_chi2 = chisquare(observed_freq, expected_freq)

print(f"Prueba de frecuencia (Chi-cuadrado): estadístico={chi2_stat}, p-valor={p_val_chi2}")



# Prueba de Kolmogorov-Smirnov
# Convertir la lista de números LCG a una escala [0, 1]
lista_lcg_normalized = [x / 100 for x in lista_lcg]

# Realizar la prueba de Kolmogorov-Smirnov
ks_stat, p_val_ks = kstest(lista_lcg_normalized, 'uniform')
print(f"Prueba de Kolmogorov-Smirnov: estadístico={ks_stat}, p-valor={p_val_ks}")



def run_test(sequence):
    runs, n1, n2 = 0, 0, 0
    for i in range(1, len(sequence)):
        if sequence[i] >= 50:
            n1 += 1
        else:
            n2 += 1
        if sequence[i] >= 50 and sequence[i-1] < 50 or sequence[i] < 50 and sequence[i-1] >= 50:
            runs += 1
    runs += 1  # incluir el primer segmento
    return runs, n1, n2

runs, n1, n2 = run_test(lista_lcg)
expected_runs = ((2 * n1 * n2) / (n1 + n2)) + 1
var_runs = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1))
z = (runs - expected_runs) / np.sqrt(var_runs)
p_val_runs = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
print(f"Prueba de secuencias: estadístico={z}, p-valor={p_val_runs}")


# Prueba de autocorrelación con lag 1
lag = 1
autocorr, p_val_autocorr = pearsonr(lista_lcg[:-lag], lista_lcg[lag:])
print(f"Prueba de autocorrelación: autocorrelación={autocorr}, p-valor={p_val_autocorr}")


def series_test(numbers, bins=10):
    # Crear una matriz de frecuencias observadas
    counts, xedges, yedges = np.histogram2d(numbers[:-1], numbers[1:], bins=bins)
    
    # Asegurarse de que las frecuencias observadas y esperadas coincidan en la suma
    total_count = np.sum(counts)
    expected_count = total_count / (bins * bins)
    
    # Aplanar las matrices para la prueba de chi-cuadrado
    observed_freq = counts.flatten()
    expected_freq = np.full_like(observed_freq, expected_count)
    
    # Realizar la prueba de chi-cuadrado
    chi2_stat, p_val_series = chisquare(observed_freq, expected_freq)
    return chi2_stat, p_val_series

chi2_series, p_val_series = series_test(lista_lcg, bins=10)
print(f"Prueba de la serie: estadístico={chi2_series}, p-valor={p_val_series}")

#endregion

#region TESTS PARA CUADRADOS

 #TESTS PARA VERIFICACION DE GENERADORES

# Prueba de frecuencia (Chi-cuadrado)
# Definir los intervalos (bins)
observed_freq, _ = np.histogram(lista_cuadrados, bins=range(1, 102))  # 100 bins de tamaño 1 (1-100)
expected_freq = np.full_like(observed_freq, len(lista_cuadrados) / 100)

# Realizar la prueba de chi-cuadrado
chi2_stat, p_val_chi2 = chisquare(observed_freq, expected_freq)

print(f"Prueba de frecuencia (Chi-cuadrado): estadístico={chi2_stat}, p-valor={p_val_chi2}")



# Prueba de Kolmogorov-Smirnov
# Convertir la lista de números LCG a una escala [0, 1]
lista_cuadrados_normalized = [x / 100 for x in lista_cuadrados]

# Realizar la prueba de Kolmogorov-Smirnov
ks_stat, p_val_ks = kstest(lista_cuadrados_normalized, 'uniform')
print(f"Prueba de Kolmogorov-Smirnov: estadístico={ks_stat}, p-valor={p_val_ks}")



def run_test(sequence):
    runs, n1, n2 = 0, 0, 0
    for i in range(1, len(sequence)):
        if sequence[i] >= 50:
            n1 += 1
        else:
            n2 += 1
        if sequence[i] >= 50 and sequence[i-1] < 50 or sequence[i] < 50 and sequence[i-1] >= 50:
            runs += 1
    runs += 1  # incluir el primer segmento
    return runs, n1, n2

runs, n1, n2 = run_test(lista_cuadrados)
expected_runs = ((2 * n1 * n2) / (n1 + n2)) + 1
var_runs = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1))
z = (runs - expected_runs) / np.sqrt(var_runs)
p_val_runs = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
print(f"Prueba de secuencias: estadístico={z}, p-valor={p_val_runs}")


# Prueba de autocorrelación con lag 1
lag = 1
autocorr, p_val_autocorr = pearsonr(lista_cuadrados[:-lag], lista_cuadrados[lag:])
print(f"Prueba de autocorrelación: autocorrelación={autocorr}, p-valor={p_val_autocorr}")


def series_test(numbers, bins=10):
    # Crear una matriz de frecuencias observadas
    counts, xedges, yedges = np.histogram2d(numbers[:-1], numbers[1:], bins=bins)
    
    # Asegurarse de que las frecuencias observadas y esperadas coincidan en la suma
    total_count = np.sum(counts)
    expected_count = total_count / (bins * bins)
    
    # Aplanar las matrices para la prueba de chi-cuadrado
    observed_freq = counts.flatten()
    expected_freq = np.full_like(observed_freq, expected_count)
    
    # Realizar la prueba de chi-cuadrado
    chi2_stat, p_val_series = chisquare(observed_freq, expected_freq)
    return chi2_stat, p_val_series

chi2_series, p_val_series = series_test(lista_cuadrados, bins=10)
print(f"Prueba de la serie: estadístico={chi2_series}, p-valor={p_val_series}")

#endregion

#region TESTS PARA RANDOM DE PYTHON

 #TESTS PARA VERIFICACION DE GENERADORES

# Prueba de frecuencia (Chi-cuadrado)
# Definir los intervalos (bins)
observed_freq, _ = np.histogram(lista_python, bins=range(1, 102))  # 100 bins de tamaño 1 (1-100)
expected_freq = np.full_like(observed_freq, len(lista_python) / 100)

# Realizar la prueba de chi-cuadrado
chi2_stat, p_val_chi2 = chisquare(observed_freq, expected_freq)

print(f"Prueba de frecuencia (Chi-cuadrado): estadístico={chi2_stat}, p-valor={p_val_chi2}")



# Prueba de Kolmogorov-Smirnov
# Convertir la lista de números LCG a una escala [0, 1]
lista_python_normalized = [x / 100 for x in lista_python]

# Realizar la prueba de Kolmogorov-Smirnov
ks_stat, p_val_ks = kstest(lista_python_normalized, 'uniform')
print(f"Prueba de Kolmogorov-Smirnov: estadístico={ks_stat}, p-valor={p_val_ks}")



def run_test(sequence):
    runs, n1, n2 = 0, 0, 0
    for i in range(1, len(sequence)):
        if sequence[i] >= 50:
            n1 += 1
        else:
            n2 += 1
        if sequence[i] >= 50 and sequence[i-1] < 50 or sequence[i] < 50 and sequence[i-1] >= 50:
            runs += 1
    runs += 1  # incluir el primer segmento
    return runs, n1, n2

runs, n1, n2 = run_test(lista_python)
expected_runs = ((2 * n1 * n2) / (n1 + n2)) + 1
var_runs = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / (((n1 + n2) ** 2) * (n1 + n2 - 1))
z = (runs - expected_runs) / np.sqrt(var_runs)
p_val_runs = 2 * (1 - scipy.stats.norm.cdf(abs(z)))
print(f"Prueba de secuencias: estadístico={z}, p-valor={p_val_runs}")


# Prueba de autocorrelación con lag 1
lag = 1
autocorr, p_val_autocorr = pearsonr(lista_python[:-lag], lista_python[lag:])
print(f"Prueba de autocorrelación: autocorrelación={autocorr}, p-valor={p_val_autocorr}")


def series_test(numbers, bins=10):
    # Crear una matriz de frecuencias observadas
    counts, xedges, yedges = np.histogram2d(numbers[:-1], numbers[1:], bins=bins)
    
    # Asegurarse de que las frecuencias observadas y esperadas coincidan en la suma
    total_count = np.sum(counts)
    expected_count = total_count / (bins * bins)
    
    # Aplanar las matrices para la prueba de chi-cuadrado
    observed_freq = counts.flatten()
    expected_freq = np.full_like(observed_freq, expected_count)
    
    # Realizar la prueba de chi-cuadrado
    chi2_stat, p_val_series = chisquare(observed_freq, expected_freq)
    return chi2_stat, p_val_series

chi2_series, p_val_series = series_test(lista_python, bins=10)
print(f"Prueba de la serie: estadístico={chi2_series}, p-valor={p_val_series}")

#endregion

#region HISTOGRAMAS

#GRAFICA DE DISTRIBUCIONES LCG 
# Configurar el diseño del gráfico
plt.figure(figsize=(10, 6))

# Generar el histograma para el generador LCG
plt.hist(lista_lcg, bins=range(1, 102), alpha=0.7, color='blue', edgecolor='black', label='LCG')

# Configurar etiquetas y título
plt.xlabel('Número Aleatorio')
plt.ylabel('Frecuencia')
plt.title('Distribución de Números Aleatorios Generados por el LCG')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()

#GRAFICA DE DISTRIBUCIONES METODO DE LOS CUADRADOS
# Configurar el diseño del gráfico
plt.figure(figsize=(10, 6))

# Generar el histograma para el generador de los cuadrados
plt.hist(lista_cuadrados, bins=range(1, 102), alpha=0.7, color='blue', edgecolor='black', label='Metodo de los cuadrados')

# Configurar etiquetas y título
plt.xlabel('Número Aleatorio')
plt.ylabel('Frecuencia')
plt.title('Distribución de Números Aleatorios Generados por el generador de los cuadrados')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()

#GRAFICA DE DISTRIBUCIONES RANDOM
# Configurar el diseño del gráfico
plt.figure(figsize=(10, 6))

# Generar el histograma para el generador Random de Python
plt.hist(lista_python, bins=range(1, 102), alpha=0.7, color='blue', edgecolor='black', label='Método Random de python')

# Configurar etiquetas y título
plt.xlabel('Número Aleatorio')
plt.ylabel('Frecuencia')
plt.title('Distribución de Números Aleatorios Generados por el generador Random de python')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
#endregion