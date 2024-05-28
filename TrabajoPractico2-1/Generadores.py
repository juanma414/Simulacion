import matplotlib.pyplot as plt
import random

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

# Generar una lista de números aleatorios
random_numbers = [lcg.next_in_range(1, 100) for _ in range(100000)]

#print(random_numbers)
# Crear un gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(range(len(random_numbers)), random_numbers, s=1)
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
seed = 1111  # Semilla inicial
n_digits = 4  # Número de dígitos de la semilla
ms = MiddleSquare(seed, n_digits)

# Generar una lista de números aleatorios en el rango 1-100
random_numbers = [ms.next_in_range(1, 100) for _ in range(100000)]

#print(random_numbers)
# Crear un gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(range(len(random_numbers)), random_numbers, s=1)
plt.title('Números Generados por el Método de la Parte Media del Cuadrado')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()


#METODO RANDOM DE PYTHON

# Generar una lista de números aleatorios entre 1 y 100
random_numbers = [random.randint(1, 100) for _ in range(100000)]
#print(random_numbers)

# Crear un gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(range(len(random_numbers)), random_numbers, s=1)
plt.title('Números Generados por random de Python')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()