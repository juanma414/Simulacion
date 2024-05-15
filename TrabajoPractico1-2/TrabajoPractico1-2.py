import random
import sys
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Verificar si se proporciona el número de valores, estrategia y tipo de capital como argumento
if len(sys.argv) != 9 or sys.argv[1] != "-n" or sys.argv[3] != "-c" or sys.argv[5] != "-s" or sys.argv[7] != "-a":
    print("Uso: python programa.py -n <num_valores> -c <num_corridas> -s <estrategia (m/d/f/o)> -a <tipo_capital (i/f)>")
    sys.exit(1)

estrategia = sys.argv[6]
if estrategia not in ['m', 'd', 'f', 'o']:
    print("La estrategia debe ser 'm', 'd', 'f' o 'o'")
    sys.exit(1)

tipo_capital = sys.argv[8]
if tipo_capital not in ['i', 'f']:
    print("El tipo de capital debe ser 'i' (infinito) o 'f' (finito)")
    sys.exit(1)

# Obtener el número de valores, estrategia y tipo de capital de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])
num_corridas = int(sys.argv[4])
estrategia = sys.argv[6]
tipo_capital = sys.argv[8]


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


if estrategia == 'm':
    for tirada in valores_todas_tiradas:
        valores_capital_corrida = []  # Sublista para almacenar los valores del capital por cada corrida
        valores_apuesta = []          #Sublista para almacenar los valores de las apuestas por cada tiro
        cap_acotado = 500  # Reiniciar el capital acotado después de cada corrida
        cont = 0  # Reiniciar el contador después de cada corrida
        for valor in tirada:
            if verificar_color(valor):
                if cont == 0:
                    cap_acotado -= apu_inicial
                    cap_acotado += 2 * apu_inicial
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apu_inicial)
                else:
                    apuesta = min(2 ** cont, cap_acotado)
                    cap_acotado -= apuesta
                    cap_acotado += 2 * apuesta
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apuesta)
                    cont = 0
            else:
                if cont == 0:
                    cap_acotado -= apu_inicial
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apu_inicial)
                    cont += 1
                else:
                    apuesta = min(2 ** cont, cap_acotado)
                    cap_acotado -= apuesta
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apuesta)
                    cont += 1
                if cap_acotado <= 0:
                    cant_bancarrotas += 1
                    if tipo_capital == 'f':
                        break  # Se detiene si cap_acotado es cero y el tipo de capital es finito
            cap_acotado = max(0, cap_acotado)  # Asegurar que cap_acotado no sea negativo
        valores_capital_acotado.append(valores_capital_corrida)


# Metodo D'Alembert (si pierde aumenta la apuesta en 1, si gana disminuye la apuesta en 1)

if estrategia == 'd':
    valores_capital_acotado = []  # Lista para almacenar los valores del capital a medida que se realizan las tiradas
    
    for tirada in valores_todas_tiradas:
        valores_capital_corrida = []  # Sublista para almacenar los valores del capital por cada corrida
        valores_apuesta = []          #Sublista para almacenar los valores de las apuestas por cada tiro
        cap_acotado = 500  # Reiniciar el capital acotado después de cada corrida
        cont = 0  # Reiniciar el contador después de cada corrida
        for valor in tirada:
            if verificar_color(valor):
                if cont == 0:
                    cap_acotado -= apu_inicial
                    cap_acotado += 2 * apu_inicial
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apu_inicial)
                else:
                    apuesta = cont
                    cap_acotado -= apuesta
                    cap_acotado += 2 * apuesta
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apuesta)
                    cont = max(0, cont - 1)
            else:
                if cont == 0:
                    cap_acotado -= apu_inicial
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apu_inicial)
                    cont += 1
                else:
                    apuesta = min(cont, cap_acotado)
                    cap_acotado -= apuesta
                    valores_capital_corrida.append(cap_acotado)
                    valores_apuesta.append(apuesta)
                    cont += 1
                if cap_acotado <= 0:
                    cant_bancarrotas += 1
                    if tipo_capital == 'f':
                        break  # Se detiene si cap_acotado es cero y el tipo de capital es finito
            cap_acotado = max(0, cap_acotado)  # Asegurar que cap_acotado no sea negativo
        valores_capital_acotado.append(valores_capital_corrida)

# Metodo Fibonacci (si pierde aumenta la apuesta en la suma de los dos anteriores, si gana retrocede dos posiciones en la serie)
if estrategia == 'f':
    valores_capital_acotado = []  # Lista para almacenar los valores del capital a medida que se realizan las tiradas
    
    for tirada in valores_todas_tiradas:
        valores_capital_corrida = []  # Sublista para almacenar los valores del capital por cada corrida
        valores_apuesta = []          #Sublista para almacenar los valores de las apuestas por cada tiro
        cap_acotado = 500  # Reiniciar el capital acotado después de cada corrida
        apuesta_anterior = 0 # Inicializar la apuesta anterior en 0
        apuesta_actual = apu_inicial  # Inicializar la apuesta actual como la apuesta inicial
        for valor in tirada:
            if verificar_color(valor):
                cap_acotado -= apuesta_actual
                cap_acotado += 2 * apuesta_actual
                valores_capital_corrida.append(cap_acotado)
                valores_apuesta.append(apuesta_actual)
                nueva_apuesta = max(apuesta_actual - apuesta_anterior, apu_inicial)
                apuesta_anterior = max(apuesta_anterior - nueva_apuesta, 0)
                apuesta_actual = nueva_apuesta
            else:
                cap_acotado -= apuesta_actual
                valores_capital_corrida.append(cap_acotado)
                valores_apuesta.append(apuesta_actual)
                apuesta_anterior, apuesta_actual = apuesta_actual, apuesta_anterior + apuesta_actual
                if cap_acotado <= 0:
                    cant_bancarrotas += 1
                    if tipo_capital == 'f':
                        break  # Se detiene si cap_acotado es cero y el tipo de capital es finito
            cap_acotado = max(0, cap_acotado)  # Asegurar que cap_acotado no sea negativo
        valores_capital_acotado.append(valores_capital_corrida)

# Método Oscar's Grind (si pierde la apuesta se mantiene, si gana aumenta la apuesta en 1 unidad hasta sacar ganancia de 1 unidad)
if estrategia == 'o':
    valores_capital_acotado=[] # Lista para almacenar los valores del capital a medida que se realizan las tiradas
    valores_apuesta = []          #Sublista para almacenar los valores de las apuestas por cada tiro
    for tirada in valores_todas_tiradas:
        valores_capital_corrida=[] # Sublista que almacena los valores del capital por corrida
        capital_inicial = cap_acotado = 500 #Reinicia el capital acotado después de cada corrida y lo iguala al capital inicial para comparación
        apuesta = apu_inicial #Reinicia la apuesta a su valor original
        for valor in tirada:
            if verificar_color(valor):
                cap_acotado -= apuesta
                cap_acotado += 2 * apuesta
                valores_capital_corrida.append(cap_acotado)
                valores_apuesta.append(apuesta)
                if (capital_inicial > cap_acotado):
                    apuesta += 1
                else:
                    apuesta = apu_inicial
            else:
                cap_acotado -= apuesta
                valores_capital_corrida.append(cap_acotado)
                valores_apuesta.append(apuesta)
                if cap_acotado <= 0:
                    cant_bancarrotas += 1
                    if tipo_capital == 'f':
                        break # Detengo la ejecución cuando el cap_acotado es menor o igual a cero y el capital es finito
            cap_acotado = max(0, cap_acotado)  # Asegurar que cap_acotado no sea negativo
        valores_capital_acotado.append(valores_capital_corrida)



print("Valores de la ruleta en cada tirada")
print(valores_todas_tiradas)
print()
print("Valores del capital despues de cada tirada")
print(valores_capital_acotado)
print()
print("Valores de cada apuesta despues de cada tirada")
print(valores_apuesta)
if tipo_capital == 'f':
    print("la cantidad de bancarrotas fue de: ",cant_bancarrotas)

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
    if tipo_capital == 'f':
        plt.axhline(y=500, color='r', linestyle='--')  # Agregar línea horizontal en el valor 500
    plt.xlabel('Tirada')
    plt.ylabel('Capital Acotado')
    plt.title(f'Corrida {i+1}')
    plt.show()

    # Calcular la cantidad de tiradas hasta obtener un resultado favorable
    tiradas_hasta_favorable = []
    count = 0
    for tirada in valores_todas_tiradas:
        for i, valor in enumerate(tirada):
            if verificar_color(valor):
                count += 1
                tiradas_hasta_favorable.append(count)
                count = 0
            else:
                count += 1

    # Graficar las frecuencias de las tiradas hasta obtener un resultado favorable
    plt.hist(tiradas_hasta_favorable, bins=range(0, num_valores+2), align='left', rwidth=0.8)
    plt.xlabel('Tiradas')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de tiradas hasta obtener un resultado favorable')
    plt.xticks(range(0, 16))  # Modificar el rango del eje x
    plt.xlim(0, 15)  # Ajustar el límite del eje x
    plt.show()

   # Crear imagenes de apuesta por tiro, una imagen por cada corrida

    plt.plot(valores_apuesta)
    plt.xlabel('Tirada')
    plt.ylabel('Valor apuesta')
    plt.title(f'Corrida {i+1}')
    plt.show()