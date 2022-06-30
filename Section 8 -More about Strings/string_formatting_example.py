# string formatting

name = 'Alan'
place = 'Parkhill'
time = '6 pm'
food = 'nasi lemak'

# string unformat
print('Hello ' + name +', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')

# string formatted
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))
