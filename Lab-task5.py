a = "hello"
b = "b2b2b2"
c = "3g3g    "
d = a+" "+b+" "+c
print(d)

e = len(d)
print(e)
print(d[:-6])

f = d.upper()
print(f)

g= d.lower()
print(g)

h = d.title()
print(h)

i = d.strip()
j = len(i)
print(j)

print(d.isdigit())

k= d.find("3g")
print(k)

l = d.capitalize()
print(l)

m= d.isalnum()
print(m)



a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b= int(b)
print(a, type(a))
x = lambda a, b : a*b
print(x(a,b))


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

a = [2,7,10,15,8]
b = []
for x in a:
    if (x%2!=0):
        b.append(x)
print(b)


def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

print(list(x))


def square(x):
    return x * x

numbers = [5, 6, 7]

squared_numbers = list(map(square, numbers))

print(squared_numbers)

a = [[1,2,3],[4,5,6],[7,8,9]]
for row in a:
    for col in row:
        print(col, end=" ")
    print()    