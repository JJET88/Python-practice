# Multiple class
class prey:
    def flee(self):
        print("The animal is fleeing.")   

class predator:
    def hunt(self):
        print("The animal is hunting.")     

class Rabbit(prey):
    alive = True

class Hawk(predator):
    breath = True

class Fish(prey,predator):    
    swim = True

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
