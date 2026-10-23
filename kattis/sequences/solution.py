MOD = 10**9 + 7

def solve(s):
    k = s.count('?')
    pow2 = [1] * (k+1)
    for i in range(1, k+1):
        pow2[i] = pow2[i-1] * 2 % MOD
    total = 0
    count1, countq = 0, 0
    for ch in s:
        if ch == '0':
            total += count1 * pow2[k] % MOD
            total += countq * pow2[k-1] % MOD
        elif ch == '?':
            if k >= 1:
                total += count1 * pow2[k-1] % MOD
            if k >= 2:
                total += countq * pow2[k-2] % MOD
        # update counts
        if ch == '1':
            count1 += 1
        elif ch == '?':
            countq += 1
        total %= MOD
    return total % MOD
print(solve(input()))