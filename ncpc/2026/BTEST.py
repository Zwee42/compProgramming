

import sys
import math

def check(ans, guess):
    if ans == guess:
        return "correct"
    if ans < guess:
        return "lower"
    if ans > guess:
        return "higher" 
    
# def round(x):
#     return math.ceil(x) if (x/2 - math.floor(x) >= 0.5) else math.floor(x) 

def do_guess(ans):
    guess = 501
    offset = guess / 2
    i = 0
    # print("TESING: " + str(ans))
    while(i < 10):
        sys.stdout.flush()
        r = check(int(ans), round(guess))
        if r == ("correct"):
            # print("Exited correctly")
            return
        if r == "lower":
            guess = guess - offset
        if r == "higher":
            guess = guess + offset
        offset = offset / 2
        i += 1
    
    print(f"FAILED, {ans} guess {guess} rguess{round(guess)}")

for ans in range(1, 1001):
    do_guess(ans)