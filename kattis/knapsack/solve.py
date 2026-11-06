


while True:
    v = ""
    try:
        v = input()
    except:
        break        

    if (v.strip() == ""):
        break
    
    c, n = map(int, v.split())

    items = []

    for i in range(n):
        v, w = map(int, input().split())
        items.append((v,w))
        
    dp = [[0] * (c+1) for i in range(n+1)]
    
    for i in range(1, n+ 1):
        v, w = items[i-1]
        
        for cap in range(c+1):
            dp[i][cap] = dp[i-1][cap]
            if cap >= w:
                dp[i][cap] = max(dp[i][cap], dp[i-1][cap-w]+v) 
    
    w_rem = c
    chosen_is = []
    for i in range(n, 0, -1):
        if dp[i][w_rem] != dp[i-1][w_rem]:
            chosen_is.append(i-1)
            w_rem -= items[i-1][1]

    chosen_is.reverse()
    print(len(chosen_is))
    print(*chosen_is)