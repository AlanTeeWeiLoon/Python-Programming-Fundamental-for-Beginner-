print('\n1--------------------------------------------\n')
# data dictionary

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')


print('\n2--------------------------------------------\n')
# data dictionary also can use integer value

spam = {12345: 'Luggage combination', 42: 'The Answer'}
print(spam[12345])

print('\n3--------------------------------------------\n')
#dictionaries are unordered

#In list
print([1, 2, 3] == [3, 2, 1]) # false

#In dictionary
eggs = {'name': 'Alan', 'species': 'cat', 'age': 20}
ham = {'species': 'cat', 'name': 'Alan', 'age': 20}
print(eggs == ham) #true

print('\n4--------------------------------------------\n')
# in and not in

eggs = {'name': 'Alan', 'species': 'cat', 'age': 20}

print('name' in eggs) # true
print('name' not in eggs) # false

print('\n5--------------------------------------------\n')
#key(), values(), and items() dictionary methods

eggs = {'name': 'Alan', 'species': 'cat', 'age': 20}

# key() method
print(list(eggs.keys()))

# values() method
print(list(eggs.values()))


# items() method
print(list(eggs.items()))  

print('\n6--------------------------------------------\n')
#key() method in for loop

eggs = {'name': 'Alan', 'species': 'cat', 'age': 20}

for k in eggs.keys():
    print(k)
    
print('\n')
for k, v in eggs.items():
    print(k,v)
    
print('\n')
for i in eggs.items():
    print(i)
    
print('\n7--------------------------------------------\n')
# get() method

picnicItems = {'apples' : 5, 'cups': 2}

print('I am bringing ' + str(picnicItems.get('oranges', 0)) + ' to the picnic.')
# pythod will return 0 value because dictionary didnt have 'oranges'

print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' to the picnic.')
# pythod will return 5 value because 'apples' in dictionary is 5

print('\n8--------------------------------------------\n')
# setdefault() dictionary method

eggs = {'name': 'Alan', 'species': 'cat', 'age': 20}

eggs.setdefault('color', 'black')
# setdefault() used when the dictionary didnt have the 'color' key()
print(eggs)

eggs.setdefault('color', 'orange')
# setdefault() will not function when the dictionary already have the 'color' key()
print(eggs)













