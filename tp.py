import random
import sys
import matplotlib.pyplot as plt

# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 7 or sys.argv[1] != "-n" or sys.argv[3] != "-c" or sys.argv[5] != "-e":
    print("Uso: python programa.py -n <num_valores> -c <num_corridas> -e <num_elegido>")
    sys.exit(1)
    


# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])
num_corridas=int(sys.argv[4])
num_elegido=int(sys.argv[6])

# Generar los valores aleatorios entre 0 y 1 y almacenarlos en una lista
valores = [random.randint(0, 36) for _ in range(num_valores)]

#define funcion de calculo de frecuencias
def calcular_frecuencias(valores):
    # Calcular la frecuencia absoluta de cada valor
    frecuencia_absoluta = {i: valores.count(i) for i in range (37) }

    # Calcular la frecuencia relativa de cada valor
    frecuencia_relativa = {i: frecuencia_absoluta[i] / len(valores) for i in range(37) }

    return frecuencia_absoluta,frecuencia_relativa

#calcula frecuencias iniciales
frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)

# Imprimir los resultados iniciales
print("Valores generados:", valores)


print("Frecuencia absoluta de ", num_elegido, ":" ,  frecuencia_absoluta[num_elegido])


print("Frecuencia relativa de ", num_elegido, ":" ,  frecuencia_relativa[num_elegido])


# Simular la adición de nuevos valores
for _ in range(num_corridas-1):
    for _ in range(num_valores):
        nuevo_valor = random.randint(0, 36)
        valores.append(nuevo_valor)
        frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)
        print("\nNuevo valor generado:", nuevo_valor)
        print("Valores generados:", valores)
        frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores)
        print("Frecuencia absoluta de ", num_elegido, ":" ,  frecuencia_absoluta[num_elegido])
        print("Frecuencia relativa de ", num_elegido, ":" ,  frecuencia_relativa[num_elegido])

freq_absoluta_esperada= num_corridas*num_valores/36
print("frecuencia absoluta esperada:",freq_absoluta_esperada)
freq_relativa_esperada= freq_absoluta_esperada /len(valores)
print("fecuencia relativa esperada:",freq_relativa_esperada)

# Crear el histograma de frecuencias absolutas

plt.bar(num_elegido,frecuencia_absoluta[num_elegido],width=0.1)
plt.axhline(freq_absoluta_esperada, color='red', linestyle='--', linewidth=2, label='Valor Teórico Esperado')
plt.xticks([num_elegido])
plt.ylabel('Frecuencia Absoluta')
plt.title(f'Ocurrencia del evento sale el número: {num_elegido}')
plt.legend()
plt.ylim(0, 6)
plt.show()