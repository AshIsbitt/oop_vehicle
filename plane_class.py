from vehicle_class import Vehicle

class Plane(Vehicle):
    def __init__(self, n_passengers, cargo_size, colour, country_of_origin):
        super().__init__(n_passengers, cargo_size)
        self.colour = colour
        self.country_of_origin = country_of_origin


    def fly(self):
        return 'Flying'

    def land(self):
        return 'Landing'

