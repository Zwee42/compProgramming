n = int(input())

last_x = True

x = 0
y = 0

sorted_values = sorted(map(int, input().split()))

c = 0
while c < n:
    if last_x:
        x += sorted_values[n - 1 - c//2]
    else:
        y += sorted_values[c//2]
    last_x = not last_x
    c += 1

print(x * x + y * y)