# doublingtime.py    
# Name: Brittany Kyncl
# Date: 9.5.22
# Course: CSD205
# Mod 7 Assignment: Time it will take to double investment

# main program purpose message
print('\nWelcome, lets calculate how long it will take for your investment to double!\nFirst, please enter your information below...')

while True:

    # declare variables
    principal = float(input('\nEnter your initial investment: '))
    APR = float(input('Enter your annual interst rate: '))
    time = 0
    final_amount = principal

    # while loop to determine years to double p
    while final_amount < principal * 2:
        final_amount = final_amount + final_amount * float(APR)/100
        time = time + 1

    # Message to show calculation results
    print(f"\nAt a {APR}% annual interst rate, your investment of ${principal:0.2f} doubles in {time} years.\n")
    print(f"Ending amount in {time} years: ${final_amount:0.2f}\n")


    # cont. # loop to re-run main program
    while True:
        cont = str(input('Perform new calculation? (y/n): '))
        if cont.lower() in ('y', 'n'):
            break
        print('Invalid Entry')

    if cont.lower() == 'y':
        continue

    else:
        print('Goodbye')
        break
