print('\n1------------------------------------\n')
for i in [0,1,2,3]:
    print(i)

print('\n2------------------------------------\n')
print(list(range(0,100,2)))


print('\n3------------------------------------\n')
spam = list(range(0,100,2))
print(spam)

print('\n4------------------------------------\n')

supplies = ['pens', 'staples', 'rulers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is : ' + supplies[i])

print('\n5------------------------------------\n')
#multiple assignment

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size)

#or

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

print(color)

