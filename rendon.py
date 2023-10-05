import random


num = random.randint(1, 1000000000)

i = int(input("hi guess a nummber: "))

while i != num:
    if i < num:
        print("guess biger")
    else:
        print("guess lower")
    i = int(input("Guess again: "))

print("good job u got it right")


