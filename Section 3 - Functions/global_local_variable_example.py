print('1----------------------------------------------\n')
spam = 42 # global variable

def eggs():
    spam =  42 #local varaible

print('Some code here:')
print('Some more code:')


print('\n2--------------------------------------------\n')
def spam():
    eggs = 99

spam()
print(eggs) # name 'eggs' will not defined #local variable cant use in the global scope

print('\n3-------------------------------------------\n')

def a():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0 

a()# local scope cant use varaible in other local scope

print('\n4-------------------------------------------\n')

def b():
    print(eggs)

eggs = 42

b() # global variable can be use in local scope

print('\n5-------------------------------------------\n')

def c():
    eggs = 'Hello'
    print(eggs)

eggs = 42
print(eggs)

c()

print('\n6-------------------------------------------\n')

def d():
    global eggs # let python know this variable is for global scope
    eggs = 'Hello'
    print(eggs)

eggs = 42
print(eggs)

d()
