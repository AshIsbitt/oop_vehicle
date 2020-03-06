
class Vehicle:
    def __init__(self, n_passengers, cargo_size):
        self.n_passengers = n_passengers
        self.cargo_size = cargo_size

    def accelerate(self):
        return "Vroom"

    def breaking(self):
        return "Stopping"