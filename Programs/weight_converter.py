# weight converter
weight = float(input("Enter your weight::"))
unit = input("Enter a unit (kg or l)")

if unit == "kg" :
    result = weight * 2.205
    unit = "lbs"
    print(f"Your weight is {round(result,1)}{unit}")
elif unit == "l":
    result = weight / 2.205
    unit = "kgs"
    print(f"Your weight is {round(result,1)}{unit}")
else:
    print("Your unit is invailed")
