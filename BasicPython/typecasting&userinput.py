# typecasting

name ="Bro"
age = 21
gpa = 1.4
student = True

print(f"{type(name)}")
print(f"{type(age)}")
print(f"{type(gpa)}")
print(f"{type(student)}")

name = int(gpa)

print(f"{type(name)}")

age = bool(age)
print(f"{age}")
# # user input
# name = input("Enter your name? :")
# age = int(input("Enter your age?:"))
# age = age + 2
# print(f"Welcome {name} Your age is {age} years old")


num1 = 15
num2 = 4.99
total = num1 + num2
print(f"{round(total,2)}")