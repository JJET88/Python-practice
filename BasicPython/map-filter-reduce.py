# Map, Filter and Reduce
store = [("shirt",20.00),("pants",24.00),("jacket",32.00),("socket",12.00)]

# to_euro = lambda data : (data[0],data[1]*0.82)
# # to_dollar = lambda data : (data[0],data[1]/0.82)
# store_euro= list(map(to_euro,store))
# for i in store_euro:
    # print(i)


# filter(function,iterable)
shop = [("shirt",20.00),("pants",24.00),("jacket",32.00),("socket",12.00)]

# price_store = lambda data: data[1]>=24

# price = list(filter(price_store,shop))

# for i in price:
#     print(i)


                        # Reduce
import functools                        
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x*y,factorial)
print(result)





