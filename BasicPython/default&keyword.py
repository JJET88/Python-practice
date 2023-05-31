# Function

# def add(a,b):
    
#     return a+ b

# print(add(3,5))
import time

def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)


# count(30,15)

# Keyword argument
def hello(greeting,title,first,middle,last,):
    print(f"{greeting} {title} {first} {middle} {last}")

hello("hello","Mr","Harry","Jame","Potter" )    

hello("hello",middle="Jame",title="Mr.",last="Potter",first="Harry")
        

print("1","2","3","4",sep=">>")