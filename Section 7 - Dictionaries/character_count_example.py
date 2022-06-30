
print('\n1-------------------------------------------------------------------\n')
message = 'It was a bright cold day in April ,and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

print('\n2-------------------------------------------------------------------\n')
#pprint module (pretty print)

import pprint

message = 'It was a bright cold day in April ,and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

print('\n3-------------------------------------------------------------------\n')
# pprint.pformat()

message = 'It was a bright cold day in April ,and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

a = pprint.pformat(count)
# set a varaible for pprint.pformat() mainly for return a string value for the output
print(a)




