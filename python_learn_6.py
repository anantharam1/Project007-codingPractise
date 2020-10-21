'''
Read the scores of the students from a file and display the Top, Bottom and Average scores.
'''

import sys
print(len(sys.argv))
x = []
if len(sys.argv) > 2:
    with open ('scores.txt') as f:
        for line in f:
            fields = line.strip('\n').split(' ')
            x.append(int(fields[2]))
        print (x)
        Top = max(x)
        Bottom = min(x)
        Average = (sum(x)/4)
        print (Top)
        print (Bottom)
        print (Average)
else:
    print("argument missing")
