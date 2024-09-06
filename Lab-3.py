thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


sum =0
even = 0
evencount = 0
odd = 0
oddcount = 0
list1 = [2,4,3,6,7,9,5]
for i in range(len(list1)):
  if i%2 == 0:
    print(list1[i])
  sum += i
print(sum)
list2 = list1
list2.sort() 
print(list2)
for i in range(len(list2)):
  if(list2[i]%2 == 0):
    even += list2[i]
    evencount +=1
  elif(list2[i]%2 != 0):
    odd += list2[i]
    oddcount +=1 
print("summation of even: ",even, "and odd: ", odd)
print("even count: ",evencount, "oddcount: ", oddcount)