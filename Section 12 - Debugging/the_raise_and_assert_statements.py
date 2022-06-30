
# Raising your own exceptions

print('\n1---------------------------------------------\n')
#raise Exception('This is the error message!') # - the error message will be 'This is the error message!' 
# - the error message

print('\n2---------------------------------------------\n')
# boxprint program

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string og length 1.')

    if(width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)

# ***************
# *             *
# *             *
# *             *
# ***************

#boxPrint('**', 5, 16) # the error  message '"symbol" needs to a string og length 1' will pop out

#boxPrint('*', 1, 1) # the error message '"width" and "height" must be greater or equal to 2' will pop out

print('\n3---------------------------------------------\n')
# The traceback format_exc() function

import traceback

try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_log.txt','a') # an 'error_log.txt' will be open with append mode
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')
                     

print('\n4---------------------------------------------\n')
# Assertions and the assert Statement

#assert False, 'This is the error message.' # AssertionError: This is the error message.

print('\n5---------------------------------------------\n')

market_2nd = {'ns' : 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd) # AssertionError: Neither light is red!{'ns': 'yellow', 'ew': 'green'}
print(market_2nd)

























    
