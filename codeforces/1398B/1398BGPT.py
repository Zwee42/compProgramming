def alice_score(s: str) -> int:
    ones = []
    count = 0
    for c in s:
        if c == '1':
            count += 1
        else:
            if count > 0:
                ones.append(count)
                count = 0
    if count > 0:
        ones.append(count)
    ones.sort(reverse=True)
    return sum(ones[::2])

t = int(input())
for _ in range(t):
    s = input().strip()
    print(alice_score(s))
