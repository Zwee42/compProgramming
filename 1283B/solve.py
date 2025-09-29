t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    max_kids_with_more = k // 2
    rem = n % k
    print(n-rem+min(rem, max_kids_with_more))