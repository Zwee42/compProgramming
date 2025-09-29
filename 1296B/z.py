import math

n = int(input())    

def maker(x):
    return (x/10)

for i in range(n):
    x = int(input())
    total = x
    if x < 10:
        print(x)
        continue
    else: 
        while x > 0:
            x = maker(x)
            print("Now, " + str(x))
            total += x
        print(math.floor(total))