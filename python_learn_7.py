import random
'''
Enter number of dice in the format XdY, for example 3d6. Toss the dice X number of times. Display the sum of all throws. 
'''

while True:
    s = input('What would u like to roll? ')
    x = s.split('d')
    if len(x) != 2:
        print('Invalid input')
        continue
    num = x[0]
    if not num.isdigit():
        print('Invalid input')
        continue
    size = x[1]
    if not size.isdigit():
        print('Invalid input')
        continue
    total = 0
    for i in range (int(num)):
        total += random.randint(1, int(size))
    print('Rolling ' + num + ',' + size + ' sided dice with a result of ' + str(total))
        
            


