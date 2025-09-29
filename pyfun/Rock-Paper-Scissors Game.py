import random

gamechoise = random.randint(0, 2)
choise = int(input('paper(0) rock(1) scissors(2)'))

if(choise == gamechoise):
    print('draw')
elif (choise == 1 & gamechoise == 2) or (choise == 2 & gamechoise == 0) or (choise == 0 & gamechoise == 1):
    print("win")
else:
    print('lose')
