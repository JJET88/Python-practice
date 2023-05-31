# Dictionary Comprehension
# dictionary = {key: expression for (key,value) in iteration}
# dictionary = {key: expression for (key,value) in iteration   if condition}
# dictionary = {key:function(value) expression for (key,value) in iteration}

weather ={"New York":"sunny","Boston":"cloudy","Los Angeles":"sunny","Chicago":"snowing"}
sunny_weather ={key: value for (key,value) in weather.items() if value == "sunny" }

print(sunny_weather)

cities_in_F ={"New York":35, "Boston":30,"Los Angeles": 43,"Chicago": 100}

cities_in_C ={key:round( (value- 32)* 5 / 9)  for (key,value) in cities_in_F.items()}
print(cities_in_C)

cities_in_F ={"New York":35, "Boston":30,"Los Angeles": 43,"Chicago": 100}

def check_temp(value):
    if value> 40 and value <60:
        return "HOT"
    elif value > 70:
        return "SUPER HOT"
    elif value > 30:
        return "COLD"    
    else:
        return "SUPER COLD"    

cities_sunny = {key: check_temp(value) for (key,value) in cities_in_F.items()}
# print(cities_sunny)
print(f"this is list comprehension {cities_sunny}")
