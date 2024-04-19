from random import seed
from random import randint

number = randint(1,100)
guess = int(input("please guess a number from 1 to 100: "))


while True:
    if guess == number:
        print ("\nyou guessed it")
        break
    elif guess < number:
        print ("\nyou were too low. guess higher")
        guess = int(input ("please enter a guess: "))
    elif guess > number:
        print ("\nyou were too high, guess lower")
        guess = int(input ("please enter a guess: "))
