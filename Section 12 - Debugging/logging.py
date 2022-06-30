# The scripts file 'logging' have rename tp 'logging1'

print('\n1---------------------------------------\n')
# the logging.basicConfig() function

import logging1

logging1.basicConfig(level = logging1.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# the set up code of logging in Python

print('\n2---------------------------------------\n')
# Buggy Factorial (!) Program

# before debugging
import logging1
logging1.basicConfig(level = logging1.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging1.debug('Start of Program')

def factorial(n):
    logging1.debug('Start of Factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging1.debug('i is %s, total is %s' % (i, total))
        
    logging1.debug('Return value is %s' % (total))
    return total

print(factorial(5)) # 0 - wrong answer

logging1.debug('End of Program')

# after debugging
import logging1
logging1.basicConfig(level = logging1.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging1.debug('Start of Program')

def factorial(n):
    logging1.debug('Start of Factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1): # after debug we found that range have to start with '1'
        total *= i
        logging1.debug('i is %s, total is %s' % (i, total))
        
    logging1.debug('Return value is %s' % (total))
    return total

print(factorial(5)) # 120 - correct

logging1.debug('End of Program')

print('\n3---------------------------------------\n')
# logging.disable(logging.CRITICAL) - turn off all the logging message

logging1.basicConfig(level = logging1.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging1.disable(logging1.CRITICAL)

logging1.debug('Start of Program')

def factorial(n):
    logging1.debug('Start of Factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1): # after debug we found that range have to start with '1'
        total *= i
        logging1.debug('i is %s, total is %s' % (i, total))
        
    logging1.debug('Return value is %s' % (total))
    return total

print(factorial(5)) # 120 - only output without any logging message 

logging1.debug('End of Program')

print('\n4---------------------------------------\n')
# Five level of logging

# logging.debug() - lowest
# logging.info()  
# logging.warning() - 
# logging.error()
# logging.critical() - highest

print('\n5---------------------------------------\n')
# Five level of logging in logging.disable()

# logging.disable(logging.DEBUG) - turn off debug logging message
# logging.disable(logging.INFO) - turn off info logging message and below
# logging.disable(logging.WARNING) - turn off warning logging message and below
# logging.disable(logging.ERROR) - turn off info error message and below
# logging.disable(logging.CRITICAL) - turn off all the logging message








































