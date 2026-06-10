# Task - add some input validation to this
lower = 4
upper = 10


age=int(input("How old are you?"))
while age < lower or age > upper:
    print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    age=int(input("How old are you?"))

if age >= 17:
    print("you are old enough to drive")
else:
    print("you are not old enough to drive yet")