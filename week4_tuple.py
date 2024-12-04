#tuple length and type
a=(1,3,5,7,4)
print(len(a))
print(type(a))

#tuple access
print(a[-2])
print(a[2])

#tuple change
b=list(a)
b[-3]=50
a=tuple(b)
print(a)

#tuple slicing
print(a[-4:-1])

#tuple add
b.append(100)
print(b)

b.insert(2,400)
print(b)

#tuple remove
b.pop()
print(b)

b.pop(2)
print(b)

#tuple join
c=(2,4,6)
x= a+c
print(x)

#tuple loop
for i in x:
    if i==7:
        break
    print(i)