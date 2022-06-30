# Non-regular Expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

print(isPhoneNumber('012-797-1844')) # True
print(isPhoneNumber('012-797-18445')) # False
print(isPhoneNumber('Alan')) # False

message = 'Call me 012-797-1844 tomorrow, or at 014-338-1844'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number.')



#Regular Expressions
import re

message = 'Call me 012-797-1844 tomorrow, or at 014-338-1844'

# search() - to create a match object
# re.compile() function to create a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # format of phone number
mo = phoneNumRegex.search(message)
# group() - to get teh matched string
print(mo.group())

#findall()
me = phoneNumRegex.findall(message)
print(me)
