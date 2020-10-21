import sys
'''
Take command line arguments and convert them into binary and hex. 
'''


if sys.argv[2].isdigit():
    x = bin(int(sys.argv[2]))
    print (x)
    x = hex(int(sys.argv[2]))
    print (x)
if sys.argv[3:]:
    print(" incorrect no. of command line arguments")
    sys.exit()



    
