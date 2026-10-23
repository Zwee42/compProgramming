ni = int(input())

nums = input().split(" ")
cmax = 0
out = []
for i, num in enumerate(nums):
    n = int(num)
    val = n + cmax
    cmax = max(val, cmax)
    out.append(val)

print(" ".join(map(str, out)))