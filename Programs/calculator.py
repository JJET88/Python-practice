# calculator program
operator = input("Enter an operator(+,-,*,/)::")
num1 = int(input("Enter a number::"))
num2 = int(input("Enter the other number::"))

if operator == "+":
    result= num1 + num2
    print(result)
elif operator == "-":
    result= num1 - num2
    print(result)
elif operator == "*":
    result= num1 * num2
    print(result)
elif operator == "/":
    result= num1 / num2
    print(result)      
else:
    print("You must check your number and operator")          
    