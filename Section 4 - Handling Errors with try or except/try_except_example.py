print('\n1---------------------------------------------------------\n')
def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print('Error')

print(div42by(2))
print(div42by(12))
print(div42by(0)) # will return none value
print(div42by(1))

print('\n2---------------------------------------------------------\n')
print('How many cats do you have?')
numCats = input()
try:

    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number!')
