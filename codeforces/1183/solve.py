q = int(input())

for i in range(q):
    (n,k) = map(int, input().split(" "))
    a_list = list(map(int, input().split(" ")))
    sortd = sorted(a_list)
    if(sortd[n-1]-sortd[0]>2*k):
        print(-1)
    else:
        print(sortd[0]+k)    
    
    
    