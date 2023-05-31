# # List Comprehension
# list =[expression for item in iterable]
# list =[expression for item in iterable if conditional]
# list =[expression if/else for item in iterable]



# square=[]
# for i in range(1,11):
#     square.append(i*i)

# print(square)  

square =[i*i for i in range(1,11)]


students =[100,90,770,60,50,40,30,10]

# graduate = [i for i in students if i>= 40]

graduate = [i if i>=60 else False for i in students]
print(graduate)



