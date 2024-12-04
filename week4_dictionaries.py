#dictionaries
employee={
    "name":"A",
    "age" :40,
    "type":{"developer":["ios","android"]},
    "parmanent":False,
    "Salary":30000,
    100:(1,2,3),
    4.5:{6,5,True,7},
    True:1,
}
print(employee)

#dictionaries lngth type
print(len(employee))
print(type(employee))

#access type
x = employee["type"]
print(x)

#access type developer
y = employee["type"]["developer"]
print(y)

#access type developer android and its length
y = employee["type"]["developer"][1]
print(y)
print(len(y))

#access 4.5
print(employee[4.5])

#employee=true
employee["parmanent"]=True
print(employee)

#add gender
employee["gender"]="male"
print(employee)

#remove age
employee.pop("age")
print(employee)

#keys, values, items in loop
for i in employee.keys():
    print(i)

for x in employee.values():
    print(x)

for y in employee.items():
    print(y)