# cablycost.py
# Name: Brittany Kyncl
# Date: 8.31.22
# Course: CSD205
# Mod 5 Assignment: Program to calculate the cost of installing fiber optic cable at .87 per ft. or bulk discount

#Display welocme message
print("Welcome! Let's calculate the total cost of fiber optic cable installation for you.")
print()

# Get company name and required feet of cable and ensure valid entry
company = input("To begin, please enter your company name: ")
print()
while True:
    if len(company) > 0:
        break
    else:
        company = input("You did not enter a company name\n"
                        "Please enter company name:")

while True:
    try:
        feet = float(input("Please enter the total fiber optic cable to be installed in feet :"))
        break
    except ValueError:
           print("Invalid Entry")


# Reg rate is standard rate per sq. ft. Cost will be actual rate after variables are applied
reg_rate = .87
cost = ()

#If statement to evaluate for teired bulk discount rate
if feet >= 500:
    cost = .50
elif feet >= 250:
    cost = .70
elif feet >= 100:
    cost = .80
else:
    cost = reg_rate

# total_cost is calcution of input feet times determined price per foot install
total_cost = feet * cost

#Display receipt message
print()
print("Here is the calculated total installation cost for", company)
if feet >= 100:
    print("You qualify for a discounted rate of $", (format(cost, '.2f'))  , "per sq. ft.!")
else:
    print("The regular rate of $.87 per sq. ft. was applied.")
print("Total install cost for", feet, "sq. ft. will be:" " $" + str(total_cost))
print()
print("Thanks for Inquiring With Us!\n"
    "Have a great day!")
