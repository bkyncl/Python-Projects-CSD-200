# file_processing.py    
# Name: Brittany Kyncl
# Date: 9.26.22
# Course: CSD205

import os # importing os library
import sys #importing system library

print(os.getcwd())

print('\n===Welcome to the file processing program===') # program message

#function to save to specified directory
def main():

    file_name = input('Enter the file name: ') # user prompt for file name    
             
    while True: # loop to re-run file write and read in case of user error
        
        name = input('Enter your name. (First and last): ') # user prompt for file information
        address = input('Enter your address: ') # user prompt for file information
        phone_number = input('Enter your phone number with area code: ') # user prompt for file information

        # creating and opening file
        with open(os.path.join(directory, file_name), 'w') as writeFile:
            # writing to file with data separated by comma's
            writeFile.write(f'{name}, {address}, {phone_number}')

        # print statements for user validation
        print(f'\nFile Name: {file_name}') #display user file name
        print('File contents: ')

        # reading and printing file stored
        with open(os.path.join(directory, file_name), 'r') as readFile:
            for line in readFile:
                print(line.rstrip()) #display user file contents for validation

        # setting user check to change information or continue
        userValidation = input('\nIs this information correct?\nIf yes hit enter, if no enter n to make changes: ')

        if userValidation.lower() == 'n': # checking user entry
            continue
        else:
            break

# function to save to CWD
def main_2():

    fileName = input('Enter the file name: ') # user prompt for file name    

    while True: # loop to re-run file write and read in case of user error
        
        name = input('Enter your name. (First and last): ') # user prompt for file information
        address = input('Enter your address: ') # user prompt for file information
        phone_number = input('Enter your phone number with area code: ') # user prompt for file information

        # creating and opening file
        with open(fileName, 'w') as writeFile:
            # writing to file with data separated by comma's
            writeFile.write(f'{name}, {address}, {phone_number}')
            
        # print statements for user validation
        print(f'\nFile Name: {fileName}') #display user file name
        print('File contents: ')

        # reading and printing file stored
        with open(fileName, 'r') as readFile:
            for line in readFile:
                print(line.rstrip()) #display user file contents for validation
    
        # setting user check to change information or continue
        userValidation = input('\nIs this information correct?\nIf yes hit enter, if no enter n to make changes: ')

        if userValidation.lower() == 'n': # checking user entry
            continue
        else:
            break

#loop to exit or run main program
while True:

    while True: # loop to validate directory existance

        #prompt user for directory name
        directory = input('\nEnter the directory you wish to save the file: ') 

        # Checking for directory
        if os.path.isdir(directory):
            print('Directory found.') # display dir found
            main() # run function to save to specified dir
            break 
        else:
            notFound = input('Directory not found. Save to current working directory? (y/n): ') # display dir not found
            if notFound == 'y':
                main_2() #run function to save to CWD
                break
            else:
                continue # looooooop

    # program re-run message
    message = input('\nTo run program enter y, to exit hit enter: ')
    if message.lower() == 'y':
        continue
    else:
        print('\nTerminanting...')
        sys.exit() # exiting program
