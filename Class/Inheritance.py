# Inheritance and Multilevel class
class living:
    alive = True

class Animal(living):
    breath = True

    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("The dog is barking")

class Fish(Animal):
    def swim(self):
        print("The fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


dog = Dog()
fish =Fish()
hawk =Hawk()


print(dog.breath)
print(dog.alive)




