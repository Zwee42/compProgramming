l = input().split(" ")
n = int(l[0])
m = int(l[1])

cc = set()

# for i in range(n):
#     cc.append(set())

for i in range(m):
    l1 = input().split(" ")
    u = int(l1[0])
    v = int(l1[1])
    cc.add((u,v))




    # cc[u-1].add((u,v))
    
    # cc[]
    # cc[v].append(u)
    # cc[u].append(v)


print(cc)    
    # for item in v[1]:
        # print(item)
        # i = item[0]
        # vals = item[1]
        # print(i)
        # print(vals)
        
            
