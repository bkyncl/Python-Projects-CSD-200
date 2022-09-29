# dictionary.py     
# Name: Brittany Kyncl
# Date: 9.3.22
# Course: CSD205
# Mod 6 Assignment: Dictionary of 10 key value pairs. Accepting user input of key to display corresponding value.

while True:
    # Initialize dictionary containing names and phone #'s

    phone_book = {'Ada': '421-2730', 'Bob': '310-2891', 'Carol': '819-2431', 'Dan': '241-3790', 'Eric': '730-2791',
    'Fred': '210-2931', 'Greg': '310-8712', 'Hans': '271-4312', 'Ian': '314-4123', 'Jack': '431-8790'}

    # Display all key values to user

    print('Welcome to the Phone Book.\nBelow is a list of all contacts.\n')
    for x in phone_book.keys():
        print(x)

    # Display request for user input
    key = input('\nEnter a name to retreive their phone number: ')
    found = 0

    # Display value paired to key input
    for x,y in phone_book.items():
        if(x == key.title()):
            found = 1
            print('The phone number is:', y)
            break
    if(found == 0):
        print('This name is not in existing contacts.')
    
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print('invalid input')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break
    
