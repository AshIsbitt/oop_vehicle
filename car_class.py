from vehicle_class import Vehicle

class Car(Vehicle):
    def __init__(self, n_passengers, cargo_size, brand, horse_power, max_speed):
        super().__init__(n_passengers, cargo_size)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed

    def park(self):
        return "Parking"

    def honk(self):
        return "HONK HONK"