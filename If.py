name = input("Please enter your name. ")
age = int(input("How old are you,{0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enoughto vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done,You guessed it")
    else:
        print("Sorry,you have not guessed correctly.")
elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done")
    else:
        print("Sorry")
else:
    print("You got it first time")

name = input("Please enter your name:")
age = int(input("How old are you,{0}?".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18-age))

age = int(input("How old are You? "))

if (age >= 16) and (age <= 65):
    print("Have a good day at work")
    if 15 < age < 66:
            print("have a good day at work")
    if (age < 16) or (age > 65):
            print("Enter your free time")
    else:
            print("Have a good day st woek")

x = "false"
if x:
    print("x is true")

x = input("Please enter some text")
if x:
    print("You entered '{}'".format(x))
else:
    print("You did not enter anything")

age = int(input("How old are you?"))
if not(age < 18):
    print("You are old enough to vote")
    print("Please pu an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Not".format(letter))
else:
    print("I don't need that letter")

letter = input("Enter a character: ")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Akki".format(letter))
