# tuple.py
# Name: Brittany Kyncl
# Date: 8.27.22
# Course: CSD205
# Mod 4 Assignment: Creating a tuple, prtinting, looping with f strings, and loop in reverse.

# Initialize a tuple containing the 17 types of planets.
planets = ('Terrestrial Planet', 'Silicate Planet', 'Puffy Planet', 'Protoplanet', 'Ocean Planet', 
'Lava Planet', 'Iron Planet', 'Ice Planet', 'Ice Giant', 'Helium Planet', 'Gas Giant', 'Gas Dwarf', 
'Desert Planet', 'Coreless Planet', 'City Planet', 'Carbon Plane', 'Chthonian Planet')
print()

#Print entire list with single statement.
print('The 17 types of planets are:', planets)
print()

#Iterate through collection displaying output as single sentence for each planet. Using f string. 
for n in range(len(planets)):
    print(f'PLanet type #{n + 1} is: {planets[n]}')

#Reverse output with different context srting
print('\t-----------Reverse-----------')
for n in range(len(planets) - 1, -1, -1):
    print(f'\t\t\t{planets[n]} is planet type #{n +1}')
print()

#Display bonus question prompt on earth planet type. While loop statement
answer = input('BONUS QUESTION: What planet type is Earth? ')

while answer.lower() != ('terrestrial'):
    print('Incorrect. Please try again.')
    answer = input()
print('Correct! Earth is a classified as a terrestrial planet.')
