# import all the classes
from vehicle_class import Vehicle
from plane_class import Plane
from car_class import Car

# create 2 vehicle instances
vehicle1 = Vehicle(4, 6)
vehicle2 = Vehicle(12, 10)

# call methods and attributes to test
print("Testing Vehicle accelleration - expected result 'Vroom'' ")
vehicle1.accelerate()
vehicle2.accelerate()

print("Testing Vehicle breaking - expected result 'Stopping'")
vehicle1.breaking()
vehicle2.breaking()

print("Testing Vehicle with Passengers = 4 and Cargo = 6. Expected result: 4, 3")
print(vehicle1.n_passengers)
print(vehicle1.cargo_size)

print("Testing Vehicle with Passengers = 12 and Cargo = 10. Expected result: 12, 10")
print(vehicle2.n_passengers)
print(vehicle2.cargo_size)

# create 2 car instances
# make car accelerate and make them break
# make car honk and park
car1 = Car(4, 6, "Isuzu", 25, 250)
car2 = Car(12, 10, "Tesla", 84, 150)

print(car1.accelerate())
print(car2.accelerate())

print(car1.breaking())
print(car2.breaking())

print(car1.honk())
print(car2.honk())

print(car1.park())
print(car2.park())

# create 2 plane instances here
# make plane accelerate and make them break
# make plane fly and land

plane1 = Plane(300, 350, "Orange", "UK")
plane2 = Plane(500, 430, "Green", "JPN")

print(plane1.accelerate())
print(plane2.accelerate())

print(plane1.breaking())
print(plane2.breaking())

print(plane1.fly())
print(plane2.fly())

print(plane1.land())
print(plane2.land())