
import sys
import math

guess = 501
offset = guess / 2
i = 0
while(i < 10):
    # print(f"guess: {guess} rguess: {round(guess)}")
    print(round(guess))
    sys.stdout.flush()
    r = input()
    if r == ("correct"):
        exit()        
    if r == "lower":
        guess = guess - offset
    if r == "higher":
        guess = guess + offset
    offset = offset / 2
    i += 1
    