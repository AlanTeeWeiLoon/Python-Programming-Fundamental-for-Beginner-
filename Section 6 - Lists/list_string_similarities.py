print('\n1---------------------------------------------\n')
#turn string into list

a = list('hello')
print(a)


print('\n2---------------------------------------------\n')
#create new string in slices

name = 'Alan is handsome'
newName = name[0:7] + ' very ' + name[8:16]
print(newName)

print('\n3---------------------------------------------\n')
#Reference

#In string
s = 42
t = s
s = 100
print(t) # output = 42
print(s) # output = 100
 
#In List
b = [0, 1, 2, 3, 4, 5]
cheese = b
cheese[1] = 'Hello'
print(cheese) # output = [0, 'Hello', 1, 2, 3, 4, 5]
print(b) # output = [0, 'Hello', 1, 2, 3, 4, 5]

print('\n4---------------------------------------------\n')
#passing list with function call

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

print('\n5---------------------------------------------\n')
#copy.deepcopy function

import copy
c = ['A', 'B', 'C', 'D']
d = copy.deepcopy(c)
d[1] = 'AA'
print(d)

print('\n6---------------------------------------------\n')
#line continuation

e = ['apples',
     'oranges',
     'bananas',
     'cats']
print(e)

print('Four score and seven ' + \
      'years ago') # \ mean the line is continue with the next line
