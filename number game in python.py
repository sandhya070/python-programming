#my practice code
import random

n = random.randrange(1, 10)
while n <90 :
    if n <= 90:
        break
    else:
        print("Too low")
        guess  = int(input("Enter number again: "))
    print("you guessed it right!!")
##learnt code and errors debugging
run = True
while run:
    user_input = int(input('Enter Number: '))
    if user_input < 70:
        print('You won!')
        run = False
    else:
        print('try again!')
        continue
##actual python project analysed and worked

import random
n = random.randrange(1,25)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")
