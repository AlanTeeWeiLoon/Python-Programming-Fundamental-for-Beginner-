# string methods

print('\n1-----------------------------------------------\n')
# upper() and lower()

spam = 'Hello World!'
print(spam.upper())
print(spam.lower())

print('\n2-----------------------------------------------\n')

print('Enter "yes": ')
answer = input()
if answer.lower() == 'yes':
    print('play again!')
    
print('\n3-----------------------------------------------\n')
# isupper() and islower()

a = 'Hello World!'
print(a.islower()) # false


b = 'HELLO WORLD!'
print(b.isupper()) # true

c = ''
print(c.isupper()) # false
print(c.islower()) # fasle

d = '12345'
print(d.islower()) # false

e = 'Hello'
print(e.upper().isupper()) # true

print('\n4-----------------------------------------------\n')
# isalpha() - letters only

f = 'hello'
print(f.isalpha()) # true

g = 'hello1234'
print(g.isalpha()) # false

print('\n5-----------------------------------------------\n')
# isalnum() - letters and number only

h = 'hello1234'
print(h.isalnum()) # true

print('\n6-----------------------------------------------\n')
# isdecimal() - numbers only

i = '1234'
print(i.isdecimal()) # true

print('\n7-----------------------------------------------\n')
# isspace() - whitespace only

j = '    '
print(j.isspace()) # true

k = 'Hello World!'
print(k.isspace()) # false

l = 'Hello World!'
print(l[5].isspace()) # true

print('\n8-----------------------------------------------\n')
# titie() and istitle() - titlecase only 

m = 'This Is Title Case.'
print(m.istitle()) # true

n = 'hello world!'
print(n.title())

print('\n9-----------------------------------------------\n')
# startswith() and endswith()

o = 'Hello world!'
print(o.startswith('Hello')) # true
print(o.startswith('H')) # true
print(o.startswith('ello')) # fasle
print(o.endswith('world!')) # true  
print(o.endswith('world')) # fasle

print('\n10-----------------------------------------------\n')
# join()

print(','.join(['cats', 'bats', 'rats']))


print('\n\n'.join(['cats', 'bats', 'rats']))

print('\n11-----------------------------------------------\n')
# split()

p = 'My name is Alan'
print(p.split())

print(p.split('m'))

print('\n12-----------------------------------------------\n')
#ljust() - left justify and rjust() - right justify

q = 'Hello'
print(q.rjust(10))
print(q.ljust(10))
print(q.rjust(10,'*'))
print(q.ljust(25,'-'))

print('\n13-----------------------------------------------\n')
# center()

r = 'Hello'
s = 'HelloHelloHello'
print(r.center(20))
print(r.center(20,'='))
print(s.center(20,'='))

print('\n14-----------------------------------------------\n')
# strip(), rstrip(), lstrip() - only can remove value in the left and right

t = '     Hello'
print(t.strip()) # remove the space

u = '          Hello           '
print(u.strip()) # remove all space
print(u.lstrip()) # remove left space
print(u.rstrip()) # remove right space

v = 'ExpAlanAlanAlanAlanxEp'
print(v.strip('Epx')) # no arrangement required

print('\n15-----------------------------------------------\n')
# replace()

w = 'Hello world!'
print(w.replace('world','Alan'))

print('\n16-----------------------------------------------\n')
# pyperclip.copy() and pyperclip,paste()

# have to install first!
