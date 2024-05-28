import matplotlib.pyplot as plt

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

# Crear un gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(range(len(random_numbers)), random_numbers, s=1)
plt.title('Números Generados por el LCG')
plt.xlabel('Índice')
plt.ylabel('Número Aleatorio')
plt.show()
