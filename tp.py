import random
import sys
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 7 or sys.argv[1] != "-n" or sys.argv[3] != "-c" or sys.argv[5] != "-e":
    print("Uso: python programa.py -n <num_valores> -c <num_corridas> -e <num_elegido>")
    sys.exit(1)
    

# Obtener el número de valores de los argumentos de la línea de comandos
num_valores = int(sys.argv[2])
num_corridas=int(sys.argv[4])
num_elegido=int(sys.argv[6])

#Cálculo del promedio esperado
prom_esperado=0
for i in range(37):
    prom_esperado += i
prom_esperado=prom_esperado/37

# Lista para almacenar los valores generados en cada tirada
valores_todas_tiradas = []

# Realizar todas las tiradas y almacenar los valores generados
for _ in range(num_corridas):
    valores = [random.randint(0, 36) for _ in range(num_valores)]
    valores_todas_tiradas.append(valores)

#Crear lista de valores promedios + Calcular valores frecuencia absoluta y relativa + Crear lista de cantidad de tiradas + Calcular varianza
prom=0
m=0
n=1
cant_tiradas = []
valores_promedios = []
frecuencia_absoluta_valores = []
frecuencia_relativa_valores = []
valores_parciales = []
varianzas_valores = []
for i in range(num_corridas):
    for j in range(num_valores):
        prom += valores_todas_tiradas[i][j]
        valores_parciales.append(valores_todas_tiradas[i][j])
        if valores_todas_tiradas[i][j] == num_elegido: m+=1
        prom_actual = prom/(n)
        valores_promedios.append(prom_actual)
        frecuencia_absoluta_valores.append(m)
        frecuencia_relativa_valores.append(m/n)
        varianzas_valores.append(np.mean((np.array(valores_parciales)-num_elegido)**2))
        cant_tiradas.append(n)
        n+=1

#define funcion de calculo de frecuencias
def calcular_frecuencias(valores):
    # Calcular la frecuencia absoluta de cada valor
    frecuencia_absoluta = {i: valores.count(i) for i in range (37) }

    # Calcular la frecuencia relativa de cada valor
    frecuencia_relativa = {i: frecuencia_absoluta[i] / len(valores) for i in range(37) }

    return frecuencia_absoluta, frecuencia_relativa

frecuencia_absoluta_acumulada = 0
# Imprimir los resultados para todas las tiradas
for idx, valores_tirada in enumerate(valores_todas_tiradas, start=1):
    print(f"\nTirada {idx}:")
    frecuencia_absoluta, frecuencia_relativa = calcular_frecuencias(valores_tirada)
    frecuencia_absoluta_acumulada += frecuencia_absoluta[num_elegido]
    print("Valores generados:", valores_tirada)
    print("Frecuencia absoluta de", num_elegido, ":", frecuencia_absoluta[num_elegido])
    print("Frecuencia relativa de", num_elegido, ":", frecuencia_relativa[num_elegido])


freq_absoluta_esperada= (num_corridas*num_valores)/37
print("\n\nfrecuencia absoluta esperada:",freq_absoluta_esperada)
freq_relativa_esperada= freq_absoluta_esperada /len(valores*num_corridas)
print("fecuencia relativa esperada:",freq_relativa_esperada)

print(valores_todas_tiradas)

def contar_colores(numeros_ruleta):
    conteo_negros = 0
    conteo_rojos = 0
    conteo_verdes = 0

    for numero in numeros_ruleta:
        # Verificar si el número es rojo
        if (numero >= 1 and numero <= 10) or (numero >= 19 and numero <= 28):
            if numero % 2 == 1:
                conteo_rojos += 1
            else:
                conteo_negros += 1
        # Verificar si el número es negro
        elif (numero >= 11 and numero <= 18) or (numero >= 29 and numero <= 36):
            if numero % 2 == 1:
                conteo_negros += 1
            else:
                conteo_rojos += 1
        # El número es verde si es 0
        elif numero == 0:
            conteo_verdes += 1

    return conteo_negros, conteo_rojos, conteo_verdes


# Contar los colores
negros, rojos, verdes = contar_colores(valores_parciales)

print("Cantidad de números negros:", negros)
print("Cantidad de números rojos:", rojos)
print("Cantidad de números verdes:", verdes)

# Crear el histograma de frecuencias absolutas
plt.bar(num_elegido,frecuencia_absoluta_valores,width=0.1)
plt.axhline(freq_absoluta_esperada, color='red', linestyle='--', linewidth=2, label='Valor Teórico Esperado')
plt.xticks([num_elegido])
plt.ylabel('Frecuencia Absoluta')
plt.title(f'Ocurrencia del evento sale el número: {num_elegido}')
plt.legend()
plt.show()

# Histograma de frecuencias absolutas acumuladas
plt.bar(cant_tiradas,frecuencia_absoluta_valores,width=0.5)
plt.axhline(freq_absoluta_esperada, color='red', linestyle='--', linewidth=2, label='Valor Teórico Esperado')
plt.xlabel('Número de tiradas')
plt.ylabel('Frecuencia Absoluta')
plt.yticks([freq_absoluta_esperada])
plt.title(f'Ocurrencia del evento sale el número: {num_elegido}')
plt.legend()
plt.show()

# Crear gráfico valor frecuencias relativas
plt.plot(frecuencia_relativa_valores, label=f'Frecuencia relativa del número {num_elegido} respecto a n')
plt.axhline(freq_relativa_esperada, color='red', linestyle='--', linewidth=2, label='Frecuencia relativa esperada')
plt.ylabel('Valor frecuencia relativa')
plt.xlabel('Número de tiradas')
plt.title('Frecuencia Relativa')
plt.legend()
plt.show()

# Crear gráfico valor promedio de tiradas
plt.plot(valores_promedios, label='Valor promedio de las tiradas respecto a n')
plt.axhline(prom_esperado, color='red', linestyle='--', linewidth=2, label='Valor Promedio Esperado')
plt.ylabel('Valor promedio de tiradas')
plt.xlabel('Número de tiradas')
plt.title('Valor Promedio')
plt.legend()
plt.show()

print(np.sqrt(varianzas_valores))
print(varianzas_valores)

# Crear gráfico valor del desvío
plt.plot(np.sqrt(varianzas_valores), label=f'Valor del desvío del número {num_elegido}')
plt.axhline(np.sqrt(varianzas_valores[-1]), color='red', linestyle='--', linewidth=2, label='Valor del desvío esperado')
plt.title(f'Desvío del numero {num_elegido}')
plt.ylabel('Valor del desvío')
plt.xlabel('Número de tiradas')
plt.legend()
plt.show()

# Crear gráfico valor del desvío
plt.plot((varianzas_valores), label=f'Valor de la varianza del número {num_elegido}')
plt.axhline(varianzas_valores[-1], color='red', linestyle='--', linewidth=2, label='Valor de la varianza esperada')
plt.title(f'Varianza del numero {num_elegido}')
plt.ylabel('Valor de la varianza')
plt.xlabel('Número de tiradas')
plt.legend()
plt.show()



# Graficar el histograma
plt.hist(valores_parciales, bins=np.arange(-0.5, 37.5, 1), width=0.8)
plt.hist(valores_parciales, bins=[num_elegido-0.5, num_elegido+0.5], color='red', label='Número elegido',width=0.8)
plt.axhline(freq_absoluta_esperada, color='red', linestyle='--', linewidth=2, label='Valor Teórico Esperado')
plt.title('Histograma de números aleatorios de la ruleta')
plt.xlabel('Número')
plt.ylabel('Frecuencia absoluta')
plt.legend()
plt.xticks(np.arange(0, 37, 1))
plt.grid(axis='y', alpha=0.5)
plt.show()

#Crear Grafico de torta de colores de los numeros

etiquetas = ['Negros', 'Rojos', 'Verdes']
colores = ['black', 'red', 'green']
cantidades = [negros, rojos, verdes]

plt.figure(figsize=(8, 6))
plt.pie(cantidades, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90,textprops={'color': 'white'})
plt.title('Distribución de colores en todas las tiradas')
plt.axis('equal')
plt.show()

# Guardar la figura en disco
plt.savefig('histogramaFrecAbs.png')