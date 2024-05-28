import matplotlib.pyplot as plt # type: ignore
import random
import pandas as pd # type: ignore
import scipy # type: ignore
import numpy as np # type: ignore
from scipy.stats import chisquare, geom, chi2 # type: ignore


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
lista_lcg = [lcg.next_in_range(1, 100) for _ in range(10000)]

#print(random_numbers)
# Crear un gráfico de dispersión de los números generados por LCG
plt.figure(figsize=(10, 6))
plt.scatter(range(len(lista_lcg)), lista_lcg, s=1)
plt.title('Números Generados por el LCG')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()


# METODO DE LOS CUADRADOS 
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
seed = 15349803495615  # Semilla inicial (Es la semilla de 5 dígitos que genera la secuencia más larga antes de entrar en bucle)
n_digits = 14  # Número de dígitos de la semilla
ms = MiddleSquare(seed, n_digits)
lista_cuadrados = ms.next()

# Generar una lista de números aleatorios con el Método de los Cuadrados
lista_cuadrados = [ms.next_in_range(1, 100) for _ in range(100000)]

#print(random_numbers)
# Crear un gráfico de dispersión de los números generados por MS
plt.figure(figsize=(10, 6))
plt.scatter(range(len(lista_cuadrados)), lista_cuadrados, s=1)
plt.title('Números Generados por el Método de la Parte Media del Cuadrado')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()


#METODO RANDOM DE PYTHON

# Generar una lista de números aleatorios con el método por defecto de Python
lista_python = [random.randint(1, 100) for _ in range(100000)]
#print(random_numbers)

# Crear un gráfico de dispersión de los números generados por Python
plt.figure(figsize=(10, 6))
plt.scatter(range(len(lista_python)), lista_python, s=1)
plt.title('Números Generados por random de Python')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()



#TESTS PARA VERIFICACION DE GENERADORES


# TEST CHI-CUADRADO
# Realizar la prueba Chi-cuadrado
statistic, p_value = chisquare(lista_lcg)
print("Estadístico de Chi-cuadrado:", statistic)
print("Valor p:", p_value)