import math

length = int(input())

max = 0

for i in range(length):
    inp = input()
    if inp == "/":
        print(max)
    else :
        inp = int(inp)
        mod = 0
        if inp % 10 == 0:
            mod = 10
        tmp = math.ceil(inp/10)*10+mod
        if tmp > max:
            max = tmp
        print(inp)