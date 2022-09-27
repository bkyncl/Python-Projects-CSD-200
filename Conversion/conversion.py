# conversion.py    
# Name: Brittany Kyncl
# Date: 9.14.22
# Course: CSD205
# Mod 8 Assignment: Function to convert miles to kilometers.
# Mod 8 Assignment: def/call function. try/expet block(s) for input validation

# program rerun 
while True:

    # entry menu and option key
    message = ('\nThis program converts miles to kilometers and vice versa.\n')
    message += ('\nEnter 1 if you wish to convert miles to kilometers\n')
    message += ('Enter 2 if you wish to convert kilomerters to miles\n')
    print(message)

    # menu input option for conversion type
    answer = input('Enter your choice (1 or 2): ')

    if answer == '1': # enter mi to km converstion
    
        # declare m to k function
        def milestokm(miles):
            """converts miles to kilometers"""
            km = float(miles) * 1.609
            print(f"\n{miles} miles = {float(km):0.3f} kilometers")

        # valid user input check
        while True:
            try: # user input for number of miles
                miles = float(input('\nHow many miles: ')) 
                break
            except ValueError: # invalid entry message
                print('Invalid Entry. Please try again: ')

        # call m to km function
        milestokm(miles)

    elif answer == '2': # enter km to mi conversion

        # declare k to m function
        def kmtomiles(kilometers):
            """converts kilometers to miles"""
            mi = float(kilometers) / 1.609
            print(f"\n{kilometers} kilometers = {float(mi):0.3f} miles.")

        # valid user input check
        while True:
            try: # user input for number of km
                kilometers = float(input('\nHow many kilometers: ')) 
                break
            except ValueError: # invalid entry message
                print('Invalid Entry. Please try again: ')

        # call k to m function
        kmtomiles(kilometers)

    else:
        print('Invalid Entry')
    
    while True:
        restart = input('\nRun program again? (y/n): ')
        if restart.lower() in ('y', 'n'):
            break
        print('Invalid Entry')
    if restart.lower() == 'y':
        continue
    else:
        print('\nTerminating...')
        break
