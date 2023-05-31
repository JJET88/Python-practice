# For loop
# for x in (range(10,0,-1)):
#     print(x)
# print("Happy  NewYEAR")

# credit = "12-33-534232-1212-211-2"
# for y in credit:
#     print(y)


# for x in range(10):
#     if x == 5:
#         continue
#     print(x)


# Nested loop
# for x in range(5):
#     for y in range(1,13,2):
#        print(y,end=" ")
#     print()

rows = int(input("Enter the numbers of rows::"))
columns = int(input("Enter the numbers of columns::"))
symbol = input("The type of symbol::")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()


