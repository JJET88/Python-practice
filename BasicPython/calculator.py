# calculator

operator = input("Enter an operator(+,-,*,/)::")
num1 = float(input("Enter a number::"))
num2 = float(input("Enter the other number::"))

if operator == "+" :
    result = num1 + num2
    print(f"the result is {round(result,2)}")
elif operator == "-" :
    result = num1 - num2
    print(f"the result is {round(result,2)}")
elif operator == "*" :
    result = num1 * num2
    print(f"the result is {round(result,2)}")
elif operator == "/" :
    result = num1 / num2
    print(f"the result is {round(result,2)}")
else:
    print("You must check your numbers and operator")

