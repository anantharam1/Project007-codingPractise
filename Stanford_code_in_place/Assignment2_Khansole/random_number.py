# python random_numbers.py
#imports random module
import random
NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100
def main():
#print 10 random numbers
    for i in range (NUM_RANDOM):
#using random function to generate numbers
        r1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print (r1)

if __name__ == '__main__':
    main()