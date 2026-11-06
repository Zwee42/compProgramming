
x, y = map(int, input().split())

n = int(input())

h = 0
w = 0

for i in range(n):
    vals = input().split()
    l = int(vals[0])
    u = int(vals[1])
    j = float(vals[2])
    
    s = u - l
    val = s * j
    
    h+=s
    # y -= s 
    w += val
    
    

if y == h:
    print(y / w)
else:
    print((y-h) / (x-w))
    