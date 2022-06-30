import re

print('\n1-----------------------------------------------------\n')
# sub() method

word = 'Agent Alice gave the secret documents to Agent Alan.'

namesRegex = re.compile(r'Agent \w+')
a = namesRegex.findall(word)
print(a) #['Agent Alice', 'Agent Alan']

namesRegex = re.compile(r'Agent \w+')
b = namesRegex.sub('REDACTED',word) # all the string included in (r'Agent \w+') will change to 'REDACTED'
print(b) # REDACTED gave the secret documents to REDACTED.

print('\n2-----------------------------------------------------\n')
# Using \1, \2, etc in sub()

word = 'Agent Caemas gave the secret documents to Agent Alan.'

namesRegex = re.compile(r'Agent (\w)\w*') # will only return the value in '(\w)'
c = namesRegex.findall(word)
print(c) # ['C', 'A'] - 'C' from Caemas and 'A' from 'Alan'

d = namesRegex.sub(r'Agent \1****', word) # \1 means the first word in the '(\w')
print(d) # Agent C**** gave the secret documents to Agent A****.

print('\n3-----------------------------------------------------\n')
# Verbose Mode with re.VERBOSE - make the regular expression more easy to read and understand

PhoneNumRegex = re.compile(r'''
(\d\d\d-)|      # area code (without parens, with dash)
(\(\d\d\d\))    # -or- area code with parens and no dash               
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}      # extension, like x1234''',re.VERBOSE)
e = PhoneNumRegex.search('My phone number is 012-797-1844.')
print(e)

print('\n4-----------------------------------------------------\n')
# Using Multiple Options (re.I, re.DOTALL, re. VERBOSE) - just use '|' operator

PhoneNumRegex = re.compile(r'''
(\d\d\d-)|      # area code (without parens, with dash)
(\(\d\d\d\))    # -or- area code with parens and no dash               
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}      # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
f = PhoneNumRegex.search('My phone number is 012-797-1844.')
print(f)















