# Shopping cart program
foods =[]
prices =[]
total = 0

while True:
    food = input("Enter the food you would like to buy(q to quit)::")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"The price of {food}::"))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food,end=" ")

for price in prices:
    total += price

print()
print(f"Total is {total}")

