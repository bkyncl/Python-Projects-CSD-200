# banking.py    
# Name: Brittany Kyncl
# Date: 9.21.22
# Course: CSD205
# Mod 9 Assignment: Banking program. With parent class and 2 child classes. Min balance/fee application/interest rate
# For this program you must choose one of two user ID's to view and interact with their cooresponding accounts.
# To view and interact with the first account with a required balance of $200, enter 'one'
# To view and interact with the second account with a required balance of $25, enter 'two'
# Then you may select from either view balance/deposit/whithdraw/etc.. from the menu options.
# Re-running the program will re-set each account

# parent bank accoutn class
class Bank_act:
    """A simple bank account"""

    def __init__(self, act_no, bal):
        """Initialize act. no. and balance attributes"""
        self.act_no = act_no
        self.bal = bal

    def deposit(self, dep_amt):
        """add deposit amount to balance"""
        self.dep_amt = dep_amt
        self.bal = self.bal + dep_amt
        print(f'Updated Balance: ${self.bal}')

    def withdraw(self, withd):
        """deduct withdrawal from balance"""
        self.withd = withd
        if self.withd > self.bal:
            print(f'Insufficient Funds | Available Balance: ${self.bal}')
        else:
            self.bal -= self.withd
            print(f'Udated Balance: ${self.bal}')

    def getBal(self):
        """get account balance"""
        return f'\nAcct. No.: {self.act_no}\nBalance: ${self.bal}'

# child checking account class
class Checking_act(Bank_act):
    """A checking type bank account"""

    def __init__(self, act_no, bal, fees, min_bal):
        """Initialize act. no., blance, fees, and min bal attributes"""
        super().__init__(act_no, bal)
        self.fees = fees
        self.min_bal = min_bal

    def check_Min_Bal(self):
        """check for minimum balance"""
        if self.bal < self.min_bal:
            print("\n\t-------!!!WARNING!!!--------\n!!Your Account is Now Below Minimum Balance!!")
            
    def deductFees(self):
        """deduct maintenance fee"""
        self.withdraw(self.fees)
        print(f'-----!!A Fee of ${self.fees} Was Charged to {self.act_no}!!-----')


#child savings accoutn class
class Savings_act(Bank_act):
    """A savings type bank account"""

    def __init__(self, act_no, bal, int_rate):
        """Initialize act. no., blance, and interest rate attributes"""
        super().__init__(act_no, bal)
        self.int_rate = int_rate

    def addInterest(self):
        """Add interest into savings account"""
        interest = self.bal * self.int_rate
        self.deposit(interest)

    def returns(self, year):
        """See savings account balance after x years of accruied interest"""
        return f'\nYour savings account balance will be ${self.bal * (1 + self.int_rate * year)} in {year} year(s) at {self.int_rate}%'

while True: # program re-run loop

    # instantiating two checking account classes and two savings account classes
    a = Checking_act('123--Checking', 200, 5, 50)
    b = Checking_act('321--Checking', 25, 5, 50)
    c = Savings_act('122--Savings', 1000, 0.02)
    d = Savings_act('322--Savings', 15000, 0.02)

    print('\n---Banking Program---\n') # program display
    print("Please enter account holder ID\n") 
    print("--Enter 'one' to view account instance with $200 balance.--")
    print("--Enter 'two' to view account instance with $25 balance--")

    # account menu option display
    message = ('\nPlease choose an option from the menu below...')
    message += ('\nCheck Checking Account Balance = 1\n')
    message += ('Make Deposit = 2\n')
    message += ('Make Withdrawal = 3\n')
    message += ('Check Savings Account Balance = 4\n')
    message += ('Calculate Future Savings Account Returns = 5\n')

    # account one pathway function
    def main_1():

        print(message) # menu options
        
        while True: # menu input validation
            try:
                options = float(input('Enter choice: '))
            except ValueError:
                print('Invalid Entry. Enter a number')
                continue
            if options >= 1 and options <= 5:
                break
            else:
                print('Invalid Entry. Enter a number 1-5.')
        
        while True:

            if options == 1:
                print(a.getBal()) # display checkin account balance
                a.check_Min_Bal() # min bal check
                break
        
            elif options == 2:
                try:
                    a.deposit(int(input('Enter Deposit: '))) # add deposit 
                except ValueError:
                    print('Invalid Entry')
                    continue
                else:
                    break

            elif options == 3:
                try:
                    a.withdraw(float(input('Enter Withdrawal: '))) # make withdrawal
                    a.check_Min_Bal() # min bal check
                except ValueError:
                    print('Invalid Entry')
                    continue
                else:
                    break

            if options == 4:
                    print(c.getBal()) # display savings balance
                    break
            
            elif options == 5:
                try:
                    print(c.returns(int(input('\nEnter number of years: ')))) # display savings account after x yr of int rate
                except ValueError:
                    print('Invalid Entry')
                    continue
                else:
                    break
    
    # account two pathway function
    def main_2():

            print(message) # menu options
            
            while True: # menu input validation
                try:
                    options = float(input('Enter choice: '))
                except ValueError:
                    print('Invalid Entry. Enter a number')
                    continue
                if options >= 1 and options <= 5:
                    break
                else:
                    print('Invalid Entry. Enter a number 1-5.')
            
            while True:

                if options == 1:
                    print(b.getBal()) # display checkin account balance
                    b.check_Min_Bal() # min bal check
                    break
            
                elif options == 2:
                    try:
                        b.deposit(int(input('Enter Deposit: '))) # add deposit 
                    except ValueError:
                        print('Invalid Entry')
                        continue
                    else:
                        break

                elif options == 3:
                    try:
                        b.withdraw(float(input('Enter Withdrawal: '))) # make withdrawal
                        b.check_Min_Bal() # min bal check
                    except ValueError:
                        print('Invalid Entry')
                        continue
                    else:
                        break

                if options == 4:
                    print(d.getBal()) # display savings balance
                    break
                
                elif options == 5:
                    try:
                        print(d.returns(int(input('\nEnter number of years: ')))) # display savings account after x yr of int rate
                    except ValueError:
                        print('Invalid Entry')
                        continue
                    else:
                        break
            
    account = input('\nEnter choice (one/two): ') # account option input
   
    # call main account functions based on user input
    if account.lower() == 'one':
        main_1() # account instance one 
    elif account.lower() == 'two':
        main_2() # accoutn instance two
    else:
        print('Invalid Entry')

    # program re-run loop cont...
    while True:
        restart = input('\nRun program again? (y/n): ')
        if restart.lower() in ('y', 'n'):
            break
        print('Invalid Entry')
    if restart.lower() == 'y':
        continue
    else:
        print('\nTerminating...') # program termination
        break
