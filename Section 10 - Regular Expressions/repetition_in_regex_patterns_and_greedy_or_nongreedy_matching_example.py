import re

print('\n1--------------------------------------\n')
      
batRegex = re.compile(r'Bat(wo)?man') # no need like (r'Batman|Batwoman')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # Batman

me = batRegex.search('The Adventures of Batwoman')
print(me.group()) # Batwoman

ma = batRegex.search('The Adventures of Batwowowowowoman')
print(ma == None) # True - only can appear 0 or 1 time


print('\n2--------------------------------------\n')
# ? - zero or one times

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
a = phoneRegex.search('My phone number is 012-797-1844. Call me tomorrow.')
print(a.group()) # 012-797-1844

phoneRegex1 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # with '( )?'
b = phoneRegex1.search('My phone number is 797-1844. Call me tomorrow.')
print(b.group()) # 797-1844

phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # with '( )?'
c = phoneRegex2.search('My phone number is 012-797-1844. Call me tomorrow.')
print(c.group()) # 012-797-1844

print('\n3--------------------------------------\n')

expRegex  =re.compile(r'dinner\?') # want to regex object with '?' must use the slash '\'.
d = expRegex.search(' Do you want have a dinner?' )
print(d.group())

print('\n4--------------------------------------\n')
# * - zero or more

batRegex = re.compile(r'Bat(wo)*man') # with *
e = batRegex.search('The Adventures of Batwowowowowoman')
print(e.group()) # Batwowowowowoman

print('\n5--------------------------------------\n')
# + - one or more

batRegex = re.compile(r'Bat(wo)+man')
f = batRegex.search('The Adventures of Batman')
print(f == None) # True - must have at least one 'wo'

g = batRegex.search('The Adventures of Batwoman')
print(g.group()) # Batwoman

h = batRegex.search('The Adventures of Batwowowowowoman')
print(h.group()) # Batwowowowowoman

print('\n6--------------------------------------\n')
# Escaping ?, * and +

regex = re.compile(r'\+\*\?')
i = regex.search('I learned about +*? regex syntax.')
print(i.group()) # +*?

regex1 = re.compile(r'(\+\*\?)+')
j = regex1.search('I learned about +*?+*?+*?+*?+*?+*?+*? regex syntax.')
print(j.group()) # +*?+*?+*?+*?+*?+*?+*?

print('\n7--------------------------------------\n')
# {x} - exactly x

haRegex =  re.compile(r'(Ha){3}') # 'Ha' 3 times
k = haRegex.search('He said "HaHaHa"')
print(k.group()) # HaHaHa

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
l = phoneRegex.search('My number is 012-797-1844,797-1844,014-338-1844')
print(l.group()) # 012-797-1844,797-1844,014-338-1844

haRegex =  re.compile(r'(Ha){3,5}') # 'Ha' minimum 3 times and maximum 5 times
# {,5} -equal to {0,5}, {3,} -3 until ...

m = haRegex.search('He said "HaHaHa"')
print(m.group()) # HaHaHa

n = haRegex.search('He said "HaHaHaHaHaHaHa"')
print(n.group()) # HaHaHaHaHa

o = haRegex.search('He said "HaHa"')
#print(o.group()) # will error because at least 3 times 'Ha'

print('\n8--------------------------------------\n')

# greedy matching
digitRegex = re.compile(r'(\d){3,5}')
p = digitRegex.search('1234567890')
print(p.group()) # 12345 - match the maximum longest possible string as normal

# nongreedy matching
digitRegex = re.compile(r'(\d){3,5}?') # non-greedy match (with '?')
q = digitRegex.search('1234567890')
print(q.group()) # 123 - will match the smallest possible string when with '?'



