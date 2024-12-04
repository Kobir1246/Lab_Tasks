# Multiple input from user

print('output of Multiple input from user:')
print('Enter two numbers: ')
a, b = input().split()
print('Output: ', a , ' ' , b)
print('sum: ', int(a) + int(b))

print('\n')

# Conditional statement

#if else

print('Output of Conditional Statement: ')
print('Enter two numbers: ')
a, b = input().split()
if  a > b:
    print(a, ' is greater than ', b)
elif a < b:
    print(a, ' is less than ', b)
else :
    print(a, ' is equals to ', b)
    
print('\n')
    
# while loop
print('Enter a number: ')
a = input()
a = int(a)
x = 1
print('numbers from 1 to ', a , 'are: ')
while x <= a:
    print(x, end=' ')
    x = x + 1
    
    
print('\n')
    
# break in while loop


print('output of break and continue inside loop: ')
friends = ["Sabbir", "Saba", "Shehab", "Ritu", "Zerin", "Aporba"]
for x in friends:
    print(x, end=' ')
    if x == "Ritu":
        break

print('\n')


#continue in loop

friends = ["Sabbir", "Saba", "Shehab", "Ritu", "Zerin", "Aporba"]
for x in friends:
    if x == "Saba":
        continue
    print(x, end=' ')

print('\n')

# Range Function

print('output of Range Function: ')
q = int(0)
print('Numbers from 1 to 10')
for x in range(10):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)

print('\n')   


print('Numbers from 20 to 50')
for x in range(20 , 50):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n')    


print('Even Numbers from 20 to 50')
for x in range(20 , 50, 2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    



print('Numbers from 100 to 50')
for x in range(100 , 50, -2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n')