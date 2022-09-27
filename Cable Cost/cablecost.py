# cablycost.py
# Name: Brittany Kyncl
# Date: 8.21.22
# Course: CSD205
# Mod 3 Assignment: Program to calculate the cost of installing fiber optic cable at .87 per ft.

#Display welocme message

print("Welcome! Let's calculate the total cost of fiber optic cable installation")

# Get company name and required feet of cable
company = input("To begin, please enter your company name:")

while True:
    if len(company) > 0:
        break
    else:
        company = input("You did not enter a company name\n"
                        "Please enter company name:")

while True:
    try:
        feet = float(input("Please enter the total fiber optic cable you wish to be installed in feet:"))
        break
    except ValueError:
           print("Invalid Entry")

# total_cost is calcution of input feet times price per foot instal
total_cost = feet * 0.87

#Display receipt message
print("The expected intsallation price at .87 per foot is listed below")
print("Company Name: " +company)
print("Total Cost: " "$" + str(total_cost))
print("Thanks for Inquiring With Us!\n"
    "Have a great day!")
