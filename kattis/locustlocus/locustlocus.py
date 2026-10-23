import math

n = input()

e = 0

for i in range(0, int(n)):
    inp = input().split(' ')
    v = int(inp[0]) + math.lcm(int(inp[1]),  int(inp[2]))
    if e > v or e == 0:
        e = v;
print(e)
