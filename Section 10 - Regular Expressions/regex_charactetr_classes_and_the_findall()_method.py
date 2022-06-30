import re

print('\n1--------------------------------------\n')
# findall() method 

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''My phone number is 012-797-1844, 013-234-7983, 013-234-7983,
        012-232-2322, 012-797-1844 and ... .'''
a = phoneRegex.findall(resume)
print(a)
print('\n')

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
b = phoneRegex.findall(resume)
print(b)
print('\n')

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
c = phoneRegex.findall(resume)
print(c)

print('\n2--------------------------------------\n')
# character classes
# '\d' - any numeric digit from 0 to 9.
# '\D' - any character that in not a numeric digit from 0 to 9.
# '\w' - any letter, numeric digit, or the underscore character.
# '\W' - any character taht is not a letter, numeric digit, or the underscore character.
# '\s' - any space, tab, or newline character.
# '\S' - any character taht is not a space, tab, or newline character.

lyrics = '''12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing,
8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 french hens,
2 turtle doves, and 1 partridge in a pear tree'''

xmasRegex = re.compile(r'\d+\s\w+')
d = xmasRegex.findall(lyrics)
print(d)

vowelRegex = re.compile(r'[aeiou]') # equal to r'[a|e|i|o|u]'
e = vowelRegex.findall('Alan eats baby food.')
print(e) # ['a', 'e', 'a', 'a', 'o', 'o']

vowelRegex = re.compile(r'[aeiouAEIOU]') # with capital 'aeiou'
f = vowelRegex.findall('Alan eats baby food.')
print(f) # ['A', 'a', 'e', 'a', 'a', 'o', 'o']

vowelRegex = re.compile(r'[aeiouAEIOU]{2}') # double vowel
g = vowelRegex.findall('Alan eats baby food.')
print(g) # ['ea', 'oo']

vowelRegex = re.compile(r'[^aeiouAEIOU]') # '^' mean not [aeiouAEIOU]
h = vowelRegex.findall('Alan eats baby food.')
print(h) # ['l', 'n', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
