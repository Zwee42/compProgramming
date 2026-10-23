
n, c = map(int, input().split())

t = 0
l = 0

ans = 0

vals  = list(map(int, input().split()))

for cur in vals:
    if cur - l > c:
        ans = 0
    ans += 1
    l = cur

print(ans)