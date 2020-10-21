from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
'''
MOON_MULTIPLE = 0.165
def main():
    earth_weight_str = input('Enter a weight on Earth: ')
    earth_weight = float(earth_weight_str)
    moon_weight = earth_weight * MOON_MULTIPLE
    print('your weight on the moon is: ' + str(moon_weight)

# There is no need to edit code beyond this point

if __name__ == "__main__":
    main()
'''
import random
def main():
    choice = random.randint(1,6)

    if choice == 1:
        print('choice 1')


# There is no need to edit code beyond this point

if __name__ == "__main__":
    main()