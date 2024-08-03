import random
import matplotlib.pyplot as plt

class InventorySimulation:
    def __init__(self, order_cost, holding_cost, shortage_cost, reorder_point, order_quantity, initial_inventory):
        self.order_cost = order_cost
        self.holding_cost = holding_cost
        self.shortage_cost = shortage_cost
        self.reorder_point = reorder_point
        self.order_quantity = order_quantity
        self.inventory = initial_inventory
        self.total_order_cost = 0
        self.total_holding_cost = 0
        self.total_shortage_cost = 0
        self.total_costs = []

    def run(self, simulation_time):
        # Reset costs for each run
        self.total_order_cost = 0
        self.total_holding_cost = 0
        self.total_shortage_cost = 0

        for _ in range(simulation_time):
            # Generar demanda aleatoria entre 0 y 100 unidades
            demand = random.randint(0, 100)
            
            # Si el inventario es menor o igual al punto de reorden, hacemos un pedido
            if self.inventory <= self.reorder_point:
                self.total_order_cost += self.order_cost
                self.inventory += self.order_quantity
            
            # Si la demanda es mayor que el inventario, hay un faltante
            if demand > self.inventory:
                shortage = demand - self.inventory
                self.total_shortage_cost += self.shortage_cost * shortage
                self.inventory = 0
            else:
                # Si hay suficiente inventario, satisfacemos la demanda
                self.inventory -= demand

            # Calcular el costo de mantenimiento
            self.total_holding_cost += self.holding_cost * self.inventory

            # Registrar el costo total diario
            total_daily_cost = self.total_order_cost + self.total_holding_cost + self.total_shortage_cost
            self.total_costs.append(total_daily_cost)

        # Calcular los costos promedios
        avg_order_cost = self.total_order_cost / simulation_time
        avg_holding_cost = self.total_holding_cost / simulation_time
        avg_shortage_cost = self.total_shortage_cost / simulation_time
        total_cost = avg_order_cost + avg_holding_cost + avg_shortage_cost

        return avg_order_cost, avg_holding_cost, avg_shortage_cost, total_cost

def run_multiple_simulations(order_cost, holding_cost, shortage_cost, reorder_point, order_quantity, initial_inventory, simulation_time, num_runs=10):
    results = []

    for _ in range(num_runs):
        inventory_sim = InventorySimulation(order_cost, holding_cost, shortage_cost, reorder_point, order_quantity, initial_inventory)
        result = inventory_sim.run(simulation_time)
        results.append((inventory_sim.total_costs, result))

    return results

def plot_results(results, simulation_time):
    for i, (total_costs, (avg_order_cost, avg_holding_cost, avg_shortage_cost, total_cost)) in enumerate(results, 1):
        plt.plot(range(simulation_time), total_costs, label=f'Corrida {i}')
    
    plt.xlabel('Tiempo de Simulación (días)')
    plt.ylabel('Costo Total')
    plt.title('Simulación de Inventario: Costo Total por Día')
    plt.legend()
    plt.show()

def main():
    print("Ingrese los parámetros de simulación:")
    order_cost = float(input("Costo de orden: "))
    holding_cost = float(input("Costo de mantenimiento: "))
    shortage_cost = float(input("Costo de escasez: "))
    reorder_point = int(input("Punto de reorden: "))
    order_quantity = int(input("Cantidad de pedido: "))
    initial_inventory = int(input("Inventario inicial: "))
    simulation_time = int(input("Tiempo de simulación (días): "))
    num_runs = int(input("Número de corridas: "))

    # Ejecutar múltiples simulaciones
    results = run_multiple_simulations(order_cost, holding_cost, shortage_cost, reorder_point, order_quantity, initial_inventory, simulation_time, num_runs)

    # Mostrar los resultados
    for i, (_, (avg_order_cost, avg_holding_cost, avg_shortage_cost, total_cost)) in enumerate(results, 1):
        print(f"\nResultados de la simulación {i}:")
        print("Costo promedio de orden:", avg_order_cost)
        print("Costo promedio de almacenamiento:", avg_holding_cost)
        print("Costo promedio de escasez:", avg_shortage_cost)
        print("Costo total:", total_cost)
        print("---------------------------------------------------")

    # Graficar los resultados
    plot_results(results, simulation_time)

if __name__ == "__main__":
    main()
