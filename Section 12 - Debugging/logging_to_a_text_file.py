import logging1

print('\n1---------------------------------------\n')
# logging to a Text File - write logging message to a text file

logging1.basicConfig(filename = 'myProgramLog.txt', level = logging1.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# add 'filename' in the logging.basicConfig()

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
                    #     - logging message already save in the 'myProgramLog.txt' file

logging1.debug('End of Program')
