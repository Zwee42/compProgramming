import math

inp = int(input())

if(inp == 0):
    print("-999", "999")
    exit()
    
if(inp == 1):
    print("2 -1")
    exit()

if(inp == -1):
    print("-2 1")
    exit()

a = inp//2
b = math.ceil(inp/2)


print(a, b)
