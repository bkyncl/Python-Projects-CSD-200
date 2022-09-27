

# infinite loop graphic program using keyboard interrupt to break


import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent == 40:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt: # crtl+c or ctrl+z
    sys.exit()
