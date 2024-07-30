import random

class MM1Simulation:
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue = []
        self.total_customers = 0
        self.total_time_in_system = 0
        self.total_time_in_queue = 0
        self.total_denial_probability = 0

    def run(self, simulation_time):
        for _ in range(simulation_time):
            if random.random() < self.arrival_rate:
                self.queue.append(1)
            if random.random() < self.service_rate and self.queue:
                self.queue.pop(0)
                self.total_customers += 1
                self.total_time_in_system += 1
                self.total_time_in_queue += len(self.queue)
                self.total_denial_probability += int(len(self.queue) > 0)

        avg_customers_in_system = self.total_customers / simulation_time
        avg_customers_in_queue = self.total_time_in_queue / simulation_time
        avg_time_in_system = self.total_time_in_system / self.total_customers
        avg_time_in_queue = self.total_time_in_queue / self.total_customers
        server_utilization = self.total_customers / simulation_time
        denial_probability = self.total_denial_probability / simulation_time

        return avg_customers_in_system, avg_customers_in_queue, avg_time_in_system, avg_time_in_queue, server_utilization, denial_probability

class InventorySimulation:
    def __init__(self, order_cost, holding_cost, shortage_cost):
        self.order_cost = order_cost
        self.holding_cost = holding_cost
        self.shortage_cost = shortage_cost
        self.total_cost = 0

    def run(self, simulation_time):
        for _ in range(simulation_time):
            demand = random.randint(0, 100)
            order_quantity = random.randint(0, 100)
            inventory = order_quantity

            if demand > inventory:
                self.total_cost += self.order_cost + self.holding_cost * (demand - inventory)
            else:
                self.total_cost += self.holding_cost * (inventory - demand) + self.shortage_cost * (demand - inventory)

        avg_order_cost = self.order_cost
        avg_holding_cost = self.holding_cost
        avg_shortage_cost = self.shortage_cost
        total_cost = self.total_cost

        return avg_order_cost, avg_holding_cost, avg_shortage_cost, total_cost

# MM1 Simulation
arrival_rate = 0.5
service_rate = 0.4
simulation_time = 1000
mm1_sim = MM1Simulation(arrival_rate, service_rate)
avg_customers_in_system, avg_customers_in_queue, avg_time_in_system, avg_time_in_queue, server_utilization, denial_probability = mm1_sim.run(simulation_time)

print("MM1 Simulation Results:")
print("Average Customers in System:", avg_customers_in_system)
print("Average Customers in Queue:", avg_customers_in_queue)
print("Average Time in System:", avg_time_in_system)
print("Average Time in Queue:", avg_time_in_queue)
print("Server Utilization:", server_utilization)
print("Denial Probability:", denial_probability)

# Inventory Simulation
order_cost = 10
holding_cost = 2
shortage_cost = 5
simulation_time = 1000
inventory_sim = InventorySimulation(order_cost, holding_cost, shortage_cost)
avg_order_cost, avg_holding_cost, avg_shortage_cost, total_cost = inventory_sim.run(simulation_time)

print("Inventory Simulation Results:")
print("Average Order Cost:", avg_order_cost)
print("Average Holding Cost:", avg_holding_cost)
print("Average Shortage Cost:", avg_shortage_cost)
print("Total Cost:", total_cost)
