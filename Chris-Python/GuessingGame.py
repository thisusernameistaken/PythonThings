import random
a=int(input("Guess a number between 1 and 100\n"))
b=random.randrange(1,100)
z=1
while a!=b:
    if a>b:
        print 'Lower'
        z=z+1
        a=int(input('Guess again\n'))
    else:
        print 'Higher'
        z=z+1
        a=int(input("Guess again\n"))
if a==b:
    print 'You win! You took %d tries' %z

