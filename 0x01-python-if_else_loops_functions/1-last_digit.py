#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
string = "and is greater than 5"
string2 = "and is less than 6 and not 0"
if ldigit > 5:
    if number < 0:
        print("Last digit of", number, "is", ldigit * -1, string)
    else:
        print("Last digit of", number, "is", ldigit, string)
elif ldigit == 0:
    print("Last digit of", number, "is", ldigit, "and is 0")
else:
    if number < 0:
        print("Last digit of", number, "is", (ldigit * -1), string2)
    else:
        print("Last digit of", number, "is", ldigit, string2)
