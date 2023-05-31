# 2D Collection

fruits = ["apple","orange","lemon","banana"] 
vegetables =["carrot","tomato","potato"]
meat =["chicken","beef","pork"]
snack = ["pizza","hambagur","hotdog","shushi"]

groceries = [fruits,vegetables,meat,snack]

# print(groceries[1][2])
# for foods in groceries:
#     for food in foods:
#      print(food,end=" ")

num_pad =((1,2,3),(4,5,6),(7,8,9),("*",10,"#"))
print(num_pad)
for row in num_pad:
    for col in row:
        print(col,end="  ")

    print()
    
