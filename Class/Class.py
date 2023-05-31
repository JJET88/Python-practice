class Car:

    wheels =4
    def __init__(self,make,model,color):
        self.make =make
        self.model= model
        self.color = color

    def drive(self):
        print("The car is driving.")
        return self


    def stop(self):
        print("The car is stopped.")
        return self
        


car_1 = Car("Japan","Toyota","green")

print(car_1.model)
print(car_1.make)
print(car_1.color)
print(car_1.wheels)

car_1.drive()\
     .stop()


    
    