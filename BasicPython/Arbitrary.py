# Arbitrary Argument

def add(*args):
    total =0
    for arg in args:
        total +=arg
    return total

# print(add(1,2,3,4,5) )      
# print(add(10,20,30))
# print(add(5,6,3,2,9,2,91))

def address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

address(city = "Yangon",
        country = "Myanmar",
        street = "Pan-Hlaing",
        zip ="1001")        
          