n = int(input())


coins = 0


nums = list(map(int, input().split()))

vals = 1

for val in nums:
    vals *= 1 if val > 0 else -1 if val < 0 else 0
    if val > 1:
        coins += val - 1
    elif val < -1:
        coins += abs(-1 - val)
    elif val == 0:
        coins += 1


if vals < 0:
    coins += 2


print(coins)
