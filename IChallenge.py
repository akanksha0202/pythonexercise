name = input("What is your name")
age = int(input("How old are you, {0} :".format(name)))

if 18 <= age < 31:
    print("Welcome to club 18-30 holiday, {0} {1}".format(name, "!"))
else:
    print("I am sorry,our holiday are only for seriously cool person")
