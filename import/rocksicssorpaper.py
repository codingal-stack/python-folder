import random
ch = ['rock', 'paper' , 'scissors']
c = random.choice(ch)
playing = True
while playing:
    c = random.choice(ch)
    i = input('rock paper or scissors?')
    if c == i:
        print('tie')
    elif c == 'rock' and i == 'paper' or c == 'paper' and i == 'scissors' or c == 'scissors' and i == 'rock':
        print('you won :)')
    else:
        print('u lost :(')
    cho = input('do you want to play again?')
    if cho == 'no':
        break
    print(c)