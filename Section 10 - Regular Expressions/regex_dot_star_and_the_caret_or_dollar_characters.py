import re

print('\n1-----------------------------------------------\n')
# '^'

beginWithHelloRegex = re.compile(r'^Hello') # 'Hello' have to in the beginning because of '^'
a = beginWithHelloRegex.search('Hello there!')

print(a.group()) # Hello

beginWithHelloRegex = re.compile(r'^Hello')
b = beginWithHelloRegex.search('He say "Hello!"') # 'Hello' is not a start of the string
print(b == None) # True

print('\n2-----------------------------------------------\n')
# '$'

endWithWorldRegex = re.compile(r'world!$') # 'world!' have to in the end of the string because of '$'
c = endWithWorldRegex.search('Hello world!')
print(c.group()) # world!

print('\n3-----------------------------------------------\n')
# ^both$ means pattern must match the entire string

allDigitRegex = re.compile(r'^\d+$')
d = allDigitRegex.search('11234567845345') # all is digit(\d)
print(d.group()) # 11234567845345
                           
allDigitRegex = re.compile(r'^\d+$')
e = allDigitRegex.search('1123456x7845345') # with one 'x'
print(e == None) # True - not all is digit (\d)

print('\n4-----------------------------------------------\n')
# '.' - anything except newline

atRegex = re.compile(r'.at')
f = atRegex.findall('The cat in the hat that sat on the flat mat.')
print(f) # ['cat', 'hat', 'hat', 'sat', 'lat', 'mat'] - 'flat' missing 'f'

atRegex = re.compile(r'.{1,2}at') # 1 until 2 things
g = atRegex.findall('The cat in the hat that sat on the flat mat.')
print(g) # [' cat', ' hat', 'that', ' sat', 'flat', ' mat'] - 'flat' with 'f' 

print('\n5-----------------------------------------------\n')
# '.*' - dot-star to match anything
# '.*' is greedy

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
h = nameRegex.findall('First Name: Alan Last Name: Tee')
print(h) # [('Alan', 'Tee')]

print('\n6-----------------------------------------------\n')
# '.*?' is non-greedy

serve = '<To serve humans> for dinner.>'

# non-greedy match
nongreedy = re.compile(r'<(.*?)>')
i = nongreedy.findall(serve)
print(i) #['To serve humans'] 

# greedy match
greedy = re.compile(r'<(.*)>')
j = greedy.findall(serve)
print(j) # ['To serve humans> for dinner.']

print('\n7-----------------------------------------------\n')
# Making Dot Match Newlines Too (with re.DOTALL)

prime = 'Serve the piblic trust.\nProtect the innocent.\nUpload the law.'

# Without matching newlines character
dotstar = re.compile(r'.*')
k = dotstar.search(prime)
print(k.group()) # Serve the piblic trust. - All character except the newline character

# Matching newlines character
dotstar = re.compile(r'.*',re.DOTALL) # with re.DOTALL
l = dotstar.search(prime)
print(l.group()) # Serve the piblic trust.\nProtect the innocent.\nUpload the law.

print('\n8-----------------------------------------------\n')
# re.IGNORECASE

# without re.IGNORECASE
vowelRegex = re.compile(r'[aeiou]') 
m = vowelRegex.findall('Alan, why does your programming book talk about RoboCop so much?')
print(m) # only print out the lower case 'aeiou'

# with re.IGNORECASE
vowelRegex = re.compile(r'[aeiou]',re.I) 
n = vowelRegex.findall('Alan, why does your programming book talk about RoboCop so much?')
print(n) # capital 'aeiou' will also included













































