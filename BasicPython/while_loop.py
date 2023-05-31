# # While loop
# name = input("Enter your name::")
#
# while name == "":
#     print("You must write your name")
#     name = input("Enter your name")
#     print(f"hello {name}")


food =input("Enter your favourite food and f to quite::")
while not food =="f":
    print(f"You like {food}")
    food=input("Enter your favourite food and f to quite::")
print("bye")