print('\n1--------------------------------------------\n')
#index method

spam = ['hello', 'hi', 'hey', 'howdy']
print(spam.index('hello'))

print('\n2--------------------------------------------\n')
#index method with duplicate value

a = ['alan', 'caemas', 'alan', 'handsome']
print(a.index('alan')) #pythod will print the first scanned value

print('\n3--------------------------------------------\n')
#append method

b = ['cat', 'dog', 'mouse']
b.append('bat') # append in the last place of the list
print(b)

print('\n4--------------------------------------------\n')
#insert method

c = ['cat', 'dog', 'mouse']
c.insert(1, 'chicken') # insert into the specific location of list
print(c)

print('\n5--------------------------------------------\n')
# remove method

d = ['cat', 'dog', 'mouse']
d.remove('cat')
print(d)

print('\n6--------------------------------------------\n')
#remove method with duplicate value

e = ['cat', 'dog', 'mouse', 'cat', 'dog', 'mouse']
e.remove('dog') # pythod only remove the first scanned value
print(e)

print('\n7--------------------------------------------\n')
#sort method

f = [2,4,6,4,8,9,5]
f.sort()
print(f)

print('\n8--------------------------------------------\n')
g = ['cat', 'dog', 'mouse', 'chicken', 'bat']
g.sort() # sort with a~z
print(g)

print('\n9--------------------------------------------\n')
h = ['cat', 'dog', 'mouse', 'chicken', 'bat']
h.sort(reverse = True) #sort with z~a
print(h)

print('\n10--------------------------------------------\n')
#ASCII medical
i = ['cat', 'dog', 'mouse', 'chicken', 'bat', 'Alan', 'Ben', 'Zion']
i.sort() # Capital letter will come first
print(i)

print('\n11--------------------------------------------\n')
j = ['a', 'z', 'c', 'A', 'C', 'Z']
j.sort(key=str.lower) # sort acccording to a~z ignoring Capital letter
print(j)

print('\n12--------------------------------------------\n')
k = ['cat', 'dog', 'mouse', 'chicken', 'bat', 'Alan', 'Ben', 'Zion']
k.sort(key=str.lower)
print(k)
