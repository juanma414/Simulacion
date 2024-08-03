import random
import matplotlib.pyplot as plt

# Lista para almacenar los resultados de las simulaciones
resultados_simulaciones = []

class MM1Simulation:
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue = []
        self.total_customers = 0
        self.total_time_in_system = 0
        self.total_time_in_queue = 0
        self.total_denial_probability = 0
        self.arrival_times = []  # Lista para almacenar los tiempos de llegada de los clientes

    def run(self, simulation_time):
        for current_time in range(simulation_time):
            if random.random() < self.arrival_rate:
                self.queue.append(current_time)  # Almacenar el tiempo de llegada
                self.arrival_times.append(current_time)
            if random.random() < self.service_rate and self.queue:
                arrival_time = self.queue.pop(0)
                self.total_customers += 1
                time_in_system = current_time - arrival_time
                self.total_time_in_system += time_in_system
                self.total_time_in_queue += len(self.queue)
                self.total_denial_probability += int(len(self.queue) > 0)

        avg_customers_in_system = self.total_customers / simulation_time
        avg_customers_in_queue = self.total_time_in_queue / simulation_time
        avg_time_in_system = self.total_time_in_system / self.total_customers if self.total_customers > 0 else 0
        avg_time_in_queue = self.total_time_in_queue / self.total_customers if self.total_customers > 0 else 0
        server_utilization = self.total_customers / simulation_time
        denial_probability = self.total_denial_probability / simulation_time

        return avg_customers_in_system, avg_customers_in_queue, avg_time_in_system, avg_time_in_queue, server_utilization, denial_probability

# Solicitar al usuario que ingrese la tasa de arribo
input_rate = input("Ingrese la tasa de arribo (25/50/75/100/125 %): ")

# Convertir la entrada a un valor numérico
try:
    input_rate = int(input_rate)
except ValueError:
    print("Por favor, ingrese un valor numérico válido.")
    exit(1)

# Asignar el valor correspondiente a arrival_rate
if input_rate == 25:
    arrival_rate = 0.1
elif input_rate == 50:
    arrival_rate = 0.2
elif input_rate == 75:
    arrival_rate = 0.3
elif input_rate == 100:
    arrival_rate = 0.4
elif input_rate == 125:
    arrival_rate = 0.5
else:
    print("Por favor, ingrese uno de los valores especificados (25/50/75/100/125).")
    exit(1)
    
# Define the function simulacion_mm1
def simulacion_mm1():
    # MM1 Simulation
    arrival_rate = 0.5 #random.uniform(0.25, 1.25)
    service_rate = 0.4
    simulation_time = 100
    mm1_sim = MM1Simulation(arrival_rate, service_rate)
    avg_customers_in_system, avg_customers_in_queue, avg_time_in_system, avg_time_in_queue, server_utilization, denial_probability = mm1_sim.run(simulation_time)

    resultado = {
        'avg_customers_in_system': avg_customers_in_system,
        'avg_customers_in_queue': avg_customers_in_queue,
        'avg_time_in_system': avg_time_in_system,
        'avg_time_in_queue': avg_time_in_queue,
        'server_utilization': server_utilization,
        'denial_probability': denial_probability
        
    }

    return resultado
# Realizar 10 corridas de la simulación
for i in range(10):
    # Ejecutar la simulación
    resultado = simulacion_mm1()
    if resultado is not None:
        resultados_simulaciones.append(resultado)
    
# Inicializar listas para cada métrica
promedio_clientes_sistema = []
promedio_clientes_cola = []
tiempo_promedio_sistema = []
tiempo_promedio_cola = []
utilizacion_servidor = []
probabilidad_denegacion = []

# Extraer los datos para cada métrica, verificando la existencia de las claves
for res in resultados_simulaciones:
    if 'avg_customers_in_system' in res:
        promedio_clientes_sistema.append(res['avg_customers_in_system'])
    if 'avg_customers_in_queue' in res:
        promedio_clientes_cola.append(res['avg_customers_in_queue'])
    if 'avg_time_in_system' in res:
        tiempo_promedio_sistema.append(res['avg_time_in_system'])
    if 'avg_time_in_queue' in res:
        tiempo_promedio_cola.append(res['avg_time_in_queue'])
    if 'server_utilization' in res:
        utilizacion_servidor.append(res['server_utilization'])
    if 'denial_probability' in res:
        probabilidad_denegacion.append(res['denial_probability'])

# Crear un gráfico con 6 subgráficos


# Promedio de clientes en el sistema
plt.plot(promedio_clientes_sistema, marker='o')
plt.title('Promedio de clientes en el sistema')
plt.xlabel('Corrida')
plt.ylabel('Promedio de clientes')
plt.show()

# Promedio de clientes en la cola
plt.plot(promedio_clientes_cola, marker='o')
plt.title('Promedio de clientes en la cola')
plt.xlabel('Corrida')
plt.ylabel('Promedio de clientes')
plt.show()
# Tiempo promedio en el sistema
plt.plot(tiempo_promedio_sistema, marker='o')
plt.title('Tiempo promedio en el sistema')
plt.xlabel('Corrida')
plt.ylabel('Tiempo promedio')
plt.show()
# Tiempo promedio en la cola
plt.plot(tiempo_promedio_cola, marker='o')
plt.title('Tiempo promedio en la cola')
plt.xlabel('Corrida')
plt.ylabel('Tiempo promedio')
plt.show()
# Utilización del servidor
plt.plot(utilizacion_servidor, marker='o')
plt.title('Utilización del servidor')
plt.xlabel('Corrida')
plt.ylabel('Utilización')
plt.show()
# Probabilidad de denegación de servicio
plt.plot(probabilidad_denegacion, marker='o')
plt.title('Probabilidad de denegación de servicio')
plt.xlabel('Corrida')
plt.ylabel('Probabilidad')
plt.show()

