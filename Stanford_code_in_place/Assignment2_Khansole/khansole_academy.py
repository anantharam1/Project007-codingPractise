# import module
import random
NUM_CORRECT = 3
MIN_RANDOM = 10
MAX_RANDOM = 99
def main():
    p = 0
    while p < NUM_CORRECT:
        r1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        r2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        y = r1+r2
        print('What is ' + str(r1) + str(' + ') + str(r2) +'? ')
        x = input ('Your answer: ')
        x = int(x)
#checking if the answer given by user is correct
        if x == y:
#check if three consecutive answers given by the user are correct
            if p == 0:
                z = 1
                print ("Correct! You've gotten " + str(z) + " correct in a row")
            if  p == 1:
                z = 2
                print ("Correct! You've gotten " + str(z) + " correct in a row")
            if p == 2:
                z = 3
                print ("Correct! You've gotten " + str(z) + " correct in a row")
                print ("Congratulations! You mastered addition.")
            p = p+1
        else:
#set the counter p to zero.
            p = 0
            print ('Incorrect. The expected answer is ' + str(y))
if __name__ == '__main__':
    main()