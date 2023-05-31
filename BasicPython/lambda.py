# Lambda function => 
# def sum(x,y):
#     return x + y

# print(sum(3,7))


sum = lambda x,y : x+y
print(sum(19,19))
square = lambda x : x*2
print(square(3))

multiple = lambda x,y:x*y
print(multiple(12,2))

full_name = lambda first,second : first+ " " +second
print(full_name("bro","code"))

age_check = lambda age :True if age>= 18 else False
print(age_check(20))
