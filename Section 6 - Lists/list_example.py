#location of list
print('\n1----------------------------------------------\n')
spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0])
print(spam[1])
print(spam[2])

#lists of lists
print('\n2----------------------------------------------\n')
a = [['cat', 'bat'], ['rat', 'elephant'], [10,20,30,40,50]]

print(a[0])
print(a[1][0])
print(a[2][4])

#negative indexes
print('\n3----------------------------------------------\n')
b = ['cat', 'bat', 'rat', 'elephant']

print(spam[-1])
print(spam[-2])

#change a list item
print('\n3----------------------------------------------\n')
c = [10, 20, 30]
c[1] = 'hello'
print(c)

d = [10, 20, 30, 40]
d[1:3] = ['cat', 'bat', 'rat']
print(d)

#del statement
print('\n4----------------------------------------------\n')
e = [10, 20, 30, 40, 50]
del e[2]
print(e)

#in and not in operator
print('\n5----------------------------------------------\n')
f = 'howdy' in ['hello', 'hi', 'howdy', 'hey']
print(f)
