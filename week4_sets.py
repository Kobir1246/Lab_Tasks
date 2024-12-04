#Sets
a={1,3,5,8,3,2}
b={0,False,1,5}
print(a)
print(b)

#Sets lenght and type
print(len(a))
print(type(a))
print(len(b))
print(type(b))

#Sets add items
a.add(10)
print(a)

#Sets remove items
a.remove(8)
print(a)

#Sets union
c=a.union(b)
print(c)

#Sets intersections
d=a.intersection(b)
print(d)

#Sets difference 
e=a.difference(b)
print(e)

#Sets join
x={2,3,4}
y= a|x
print(y)

#Sets loop
for i in y:
  print(i)

#Sets if found 3 print it
if 3 in a:
  print("3 is pressent")