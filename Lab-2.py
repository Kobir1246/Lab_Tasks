list1 = ["apple", "banana", "cherry"]
print(list1)


list2 = list(("apple", "banana", "cherry","apple"))
print(list2)


list3 = ["apple", "banana", "cherry"]
print(list3[1])


list4 = ["apple", "banana", "cherry"]
print(list4[-1])


list5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list5[2:5])
print(list5[:4])
print(list5[4:])
if "banana" in list5:
    print("Yes")


list6 = ["apple", "banana", "cherry"]
list6[1] = "blackcurrant"
print(list6)


list7 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list7[1:3] = ["blackcurrant", "watermelon"]
print(list7)


list8 = ["apple", "banana", "cherry"]
list8[1:2] = ["blackcurrant", "watermelon"]
print(list8)


list9 = ["apple", "banana", "cherry"]
list9.insert(2, "watermelon")
print(list9)


list10 = ["apple", "banana", "cherry"]
list10.append("orange")
print(list10)


list11 = ["apple", "banana", "cherry"]
list11.insert(1, "orange")
print(list11)


list12 = ["apple", "banana", "cherry"]
t = ["mango", "pineapple", "papaya"]
list12.extend(t)
print(list12)
list12.remove("banana")
print(list12)


list13 = ["apple", "banana", "cherry"]
list13.pop(1)
print(list13)


list14 = ["apple", "banana", "cherry"]
for x in list14:
  print(x)


list15 = ["apple", "banana", "cherry"]
for i in range(len(list15)):
  print(list15[i])


list16 = ["apple", "banana", "cherry"]
i = 0
while i < len(list16):
  print(list16[i])
  i = i + 1


fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
list17 = []
for x in fruit:
  if "a" in x:
    list17.append(x)
print(list17)