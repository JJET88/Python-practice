# Temperature conversion
temp = float(input("Enter the temperature::"))
unit = input("Enter Farenheit(F) or Celsius(C)::")

if unit == "C":
    temp = (temp * 9) / 5 + 32
    print(f"The temperature is {temp:.2f} degree Farenheit")
elif unit == "F":
    temp = (temp - 32)* 5 / 9
    print(f"The temperature is {temp:.2f} degree Celsius")
