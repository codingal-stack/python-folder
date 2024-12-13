import random

s = random.randint(1,10)

playing = True
while playing:
    n = int(input('enter a number from 1 - 10'))
    if n == s:
        print('Correct!')
        break
    else:
        playing = (input("do you want to keep trying (yes or no)")) 
    if playing == 'no':
        break
    
