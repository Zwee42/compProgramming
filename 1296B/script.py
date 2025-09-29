t = int(input())

for _ in range(t):
    s = int(input())
    t = 0
    while s > 9:
        cb = s // 10
        t += cb * 10
        s = cb +  s % 10   
    print(t+s)