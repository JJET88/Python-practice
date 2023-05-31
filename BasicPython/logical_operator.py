age =int(input("Enter your age::"))

if age >= 18 and age <= 30:
    print("You are an adult")
elif age <17 :
    print("You are too young")
elif age == 0 or age < -1:
    print("You haven't born yet")
else:
    print("You are too old")


sunny = True
if not sunny:
    print("The weather is bad")
else:
    print("The weather is good")