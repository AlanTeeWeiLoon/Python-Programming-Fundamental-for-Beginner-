# group()
import re

message = 'Call me 012-797-1844 tomorrow, or at 014-338-1844'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo = phoneNumRegex.search(message)
print(mo.group()) # 012-797-1844

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # add blanket '( )'
mo = phoneNumRegex.search(message)
print(mo.group(1)) # 012
print(mo.group(2)) # 797-1844

a = 'My number is (012) 797-1844'
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(a)
print(mo.group()) # (012) 797-1844


# | Pipe Character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) # batmobile

mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo == None) # True

mo = batRegex.search('Batmotorcycle lost a wheel')
#print(mo.group()) # will error

# to find which suffixies
mo = batRegex.search('Batmobile lost a wheel, Batman lost a leg')
print(mo.group(1)) # mobile
