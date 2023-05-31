# Object as an argument  606

class Car:
    color = "green"

class Motorcycle:
    color = None

def change_color(vehicle,color):
    vehicle.color = color


car = Car()
bike = Motorcycle()            

# change_color(car,"red")
change_color(bike,"blue")

print(car.color) 
print(bike.color)
