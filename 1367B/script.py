t = int(input())
for _ in range(t):
    swaps = 0
    w_index  = []
    input()  
    n = list(map(int, input().split()))
    for index, value in enumerate(n):
        if value % 2 != index % 2:
            flag = False
            for wi in w_index:
                if wi % 2 != index % 2:
                    n[index], n[wi] = n[wi], n[index]
                    w_index.remove(wi)
                    flag = True
                    swaps += 1
                    break
            if not flag:
                w_index.append(index)
    if len(w_index) > 0:
        print(-1)
    else:
        print(swaps)
