'''
Take a command line input and divide by 2 if it is an integer.
'''


import sys
for arg in sys.argv[2:]:
    if arg.isdigit():
        x = int(arg)/2
        print (x)
    else:
        print(arg + " is not number")
