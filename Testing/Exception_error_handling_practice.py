filename = 'Test_file.txt'

with open(filename, 'w') as file_object:
    file_object.write('line one\n')
    file_object.write('line two\n')
    file_object.write('line three\n')

with open(filename,'r') as readFile:
    for line in readFile:
        print(line.rstrip())

try:
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())
except FileNotFoundError:
    print('File Not Found Error')
except NameError:
    print('Variable NameError')

print()

fileInput = 'Test_file.txt'
fileOutput = 'Output_1.txt'

try:
    with open(fileOutput, 'w') as file_objectOutput:

        with open(fileInput) as file_objectInput:
            for line in file_objectInput:
                file_objectOutput.write(line)

except FileNotFoundError:
    print('The file was not found')

except:
    print('Different types of errors')

print()

fileInput = 'Test_file.txt'

totalLines = 0

try:
    with open(fileInput) as file_objectInput:
        for line in file_objectInput:
            print(line.rstrip())
            totalLines += 1
    print()
    print()
    print(f'Total number of lines: {totalLines}')
    print()

except FileNotFoundError:
    print('File not found')

except:
    print('A diff error')

print()

try:
    print('this line will print')
    print(10/0)
    print('this line will not print')
except ZeroDivisionError:
    print('use result of 0')

print()

try:
    print('this line will print')
    print(10/0)
    print('this line will not print')
except ZeroDivisionError:
    print('user result of 0')

print()
while True:

    while True:
        firstInput = input('Enter first integer: ')
        secondInput = input('Enter second integer: ')

        try:
            firstInt = int(firstInput)
            secondInt = int(secondInput)
            assert firstInt >= 0
            assert secondInt >= 0
        except AssertionError:
            print('You must enter positive integer')
            continue
        except ValueError:
            print('You must enter integer value')
            continue

        else:
            try:
                print(f'The value {firstInt} divided by {secondInt} is {firstInt // secondInt}')
                break
            except ZeroDivisionError:
                print('We cannot divide by zero')
                continue

    if input('Run again: y/n: ') == 'y':
        continue
    else:
        break
print('\nthe end')