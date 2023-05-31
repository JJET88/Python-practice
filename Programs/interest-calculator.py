# Compound interest calculator
principal = 0
rate = 0
time =  0

while True:
    principal = float(input("Enter the principal amount::"))
    if principal < 0:
        print("Principal can't be less than zero!")
    else:
        break
    

while True:
    rate = float(input("Enter the rate ::"))    
    if rate < 0:
        print("Rate can't be less than zero!")
    else:
        break


while True:
    time = float(input("Enter the time in year::"))
    if time < 0:
        print("The time can't be less than zero!")
    else:
        break

total = principal*pow((1 + rate/100),time)

print(f"The total is {total}")