import random
import sys
import numpy as np # type: ignore
#import matplotlib.pyplot as plt # type: ignore


# Verificar si se proporciona el número de valores como argumento
if len(sys.argv) != 8 or sys.argv[1] != "-n" or sys.argv[3] != "-c" or sys.argv[5] != "-s" or sys.argv[7] != "a":
    print("Uso: python programa.py -n <num_valores> -c <num_corridas> -s <estrategia> -a <tipo_capital>")
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

# Almacenamiento del capital , apuesta inicial y contador
    cap_acotado = 500
    apu_inicial = 1
    
    cont = 0;  # se utiliza para reiniciar la apuesta a la inicial en el caso q salga rojo

# Verificar colores
def verificar_color(numero):
# El color elegido para apostar es el rojo
# Verificar si el número es rojo
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


# Metodo Martingale
for i in range(num_corridas):
    for j in range(num_valores):
        if (verificar_color(valores_todas_tiradas[i][j])):
            if(cont==0):
                cap_acotado = cap_acotado- apu_inicial          #Aca creo que se puede hacer (cap_acotado = cap_acotado + 1) en lugar de las 2 operaciones, deje las 2 para que se entienda, 
                cap_acotado = cap_acotado + 2*apu_inicial       #ya que en realidad lo que se resta es la apuesta y lo que se suma es la ganancia
                valores_capital_acotado.append(cap_acotado)
            else: 
                cap_acotado= cap_acotado - 2**cont     # Ej: si salio 1 negro, cont= 1 --> resto 2 (apuesta) y gano 4 (ganancia)
                cap_acotado= cap_acotado + 2**(cont+1)
                valores_capital_acotado.append(cap_acotado)
                cont =0;    # Aca si necesito reiniciar el contador ya que antes salio un negro para entrar en este else, osea (cont != 0)
            
        else:   
            if(cont == 0):
              cap_acotado = cap_acotado - apu_inicial;
              valores_capital_acotado.append(cap_acotado)
              cont= cont+1;
            else:
                cap_acotado= cap_acotado - 2**cont
                valores_capital_acotado.append(cap_acotado);
                cont=cont+1;


print(valores_todas_tiradas)
a = input()