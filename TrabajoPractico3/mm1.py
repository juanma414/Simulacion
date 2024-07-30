import numpy as np # type: ignore

class MM1Queue:
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.rho = arrival_rate / service_rate
        self.Lq = self.rho**2 / (1 - self.rho)
        self.Wq = self.Lq / arrival_rate
        self.Ls = self.rho / (1 - self.rho)
        self.Ws = self.Ls / arrival_rate

    def use(self):
        return self.rho

    def avg_queue_length(self):
        return self.Lq

    def avg_wait_time_in_queue(self):
        return self.Wq

    def avg_number_in_system(self):
        return self.Ls

    def avg_wait_time_in_system(self):
        return self.Ws

# Example
arrival_rate = 2  # Arrival rate (clients in time unit)
service_rate = 3  # Service rate (served clients in time unit)

queue = MM1Queue(arrival_rate, service_rate)

print(f"Server use (rho): {queue.use():.2f}")
print(f"Length in queue (Lq): {queue.avg_queue_length():.2f}")
print(f"Waiting in queue (Wq): {queue.avg_wait_time_in_queue():.2f}")
print(f"Length in system (Ls): {queue.avg_number_in_system():.2f}")
print(f"Waiting in system (Ws): {queue.avg_wait_time_in_system():.2f}")