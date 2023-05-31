# Dictionary

capitals = {"USA":"Washinting D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Mosco"}

print(capitals.get("USA"))            

capitals.update({"Japan":"Tokyo"})

# print(capitals)
# print(capitals.keys())
# print(capitals.values())        482
# print(capitals.items())

for keys,values in capitals.items():
     print(f"{keys} : {values}")

