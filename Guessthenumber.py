import random
n=random.randint(1,100)
for i in range(5):
    print('Enter guess #:',i+1)
    g=int(input('=>'))
    if g==n:
        print('You win!')
        break
    elif g>n:
        print('Try guessing smaller!')
    else:
        print('Try guessing bigger!')
else:
    print('You lose!\nThe number was:',n)
