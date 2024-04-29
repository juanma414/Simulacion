import random
import sys
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 5 or sys.argv[1] != "-n" or sys.argv[3] != "-c":
    print("Uso: python programa.py -n <num_valores> -c <num_corridas>")
    sys.exit(1)
    

# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])
num_corridas=int(sys.argv[4])


# Lista para almacenar los valores generados en cada tirada
valores_todas_tiradas = []


# Realizar todas las tiradas y almacenar los valores generados
for _ in range(num_corridas):
    valores = [random.randint(0, 36) for _ in range(num_valores)]
    valores_todas_tiradas.append(valores)

# Almacenar los valores individualmente
valores_parciales = []
for i in range(num_corridas):
    for j in range(num_valores):
        valores_parciales.append(valores_todas_tiradas[i][j])

# Lista para almacenar los valores del capital a medida que se realizan las tiradas 
    valores_capital_acotado = []

# Almacenamiento del capital , apuesta inicial , contador, bancarrotas
    cap_acotado = 500
    apu_inicial = 1
    cant_bancarrotas = 0
    cont = 0;  # se utiliza para reiniciar la apuesta a la inicial en el caso q salga rojo

# El color elegido para apostar es el rojo
# Verificar si el número es rojo
def verificar_color(numero):

    if (numero >= 1 and numero <= 10) or (numero >= 19 and numero <= 28):
        if numero % 2 == 1:
            return True
        else:
            return False
    elif (numero >= 11 and numero <= 18) or (numero >= 29 and numero <= 36):
        if numero % 2 == 1:
            return False
        else:
            return True
    elif numero == 0:
            return False

# Metodo Martingale (si pierde duplica la apuesta, si gana vuelve a la apuesta inicial)
valores_capital_acotado = []

for tirada in valores_todas_tiradas:
    valores_capital_corrida = []  # Sublista para almacenar los valores del capital por cada corrida
    cap_acotado = 500  # Reiniciar el capital acotado después de cada corrida
    cont = 0  # Reiniciar el contador después de cada corrida
    for valor in tirada:
        if verificar_color(valor):
            if cont == 0:
                cap_acotado -= apu_inicial
                cap_acotado += 2 * apu_inicial
                valores_capital_corrida.append(cap_acotado)
            else:
                apuesta = min(2 ** cont, cap_acotado)
                cap_acotado -= apuesta
                cap_acotado += 2 * apuesta
                valores_capital_corrida.append(cap_acotado)
                cont = 0
        else:
            if cont == 0:
                cap_acotado -= apu_inicial
                valores_capital_corrida.append(cap_acotado)
                cont += 1
            else:
                apuesta = min(2 ** cont, cap_acotado)
                cap_acotado -= apuesta
                valores_capital_corrida.append(cap_acotado)
                cont += 1
            if cap_acotado <= 0:
                cant_bancarrotas += 1
                break  # Se detiene si cap_acotado es cero
        cap_acotado = max(0, cap_acotado)  # Asegurar que cap_acotado no sea negativo
    valores_capital_acotado.append(valores_capital_corrida)

print(valores_todas_tiradas)
print()
print(valores_capital_acotado)
print(cant_bancarrotas)

# Calcular la ganancia total y por cada corrida
ganancia_total = 0
ganancias_por_corrida = []

for corrida in valores_capital_acotado:
    ganancia_corrida = corrida[-1] - 500
    ganancia_total += ganancia_corrida
    ganancias_por_corrida.append(ganancia_corrida)

# Mostrar ganancias
print("Ganancia total:", ganancia_total)
print("Ganancias por corrida:", ganancias_por_corrida)

# Crear imagenes de capital_acotado en cada tirada, una imagen por cada corrida
for i, corrida in enumerate(valores_capital_acotado):
    plt.plot(corrida)
    plt.xlabel('Tirada')
    plt.ylabel('Capital Acotado')
    plt.title(f'Corrida {i+1}')
    plt.show()
