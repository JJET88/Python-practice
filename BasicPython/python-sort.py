# Sort
students = [("Ussop","F",42),("Sanji","A",34),("Luffy","B",23),("Nami","C",32)]

grade = lambda grades:grades[1]
age = lambda age : age[2]
# students.sort(key=grade)
students.sort(key=age)
for i in students:
    print(i)