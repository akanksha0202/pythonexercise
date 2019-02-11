import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a numbr 1 and {}: ".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it!")