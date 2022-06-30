# using the debugger - after run(F5) click 'debug' then 'debugger'


# button in debuggeer
# - Go   - use to run the program
# - Step - move the debugger inside oa a function call if that's what about to be executed
# - Over - execute the line highlighted and then proceed to pause again before it executes the next line
# - Out  - keep executing lines until the function taht you're currently in returns
# - Quit - teminates the program immediately

print('\n1---------------------------------------\n')

# before debug
print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third + '\n') # output something wrong


# after debug
print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + str(int(first) + int(second) + int(third)) + '\n') # output after debug is correct


    

