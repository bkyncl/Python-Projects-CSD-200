dictimput = {}
print(dictimput)

entervalid = True
doagain = 'yes'

while entervalid:

    name = input('enter a name: ')
    age = input('enter an age: ')

    dictimput[name.title()] = age
    
    doagain = input('do you need to enter another? ')

    if doagain.lower() == 'no':
        entervalid = False
    elif doagain.lower() == 'yes':
        entervalid = True
    else:
        print('invalid')
        doagain = input('do you need to enter another? ')
        continue

print(dictimput)

