import collections

(n,m,k) = map(int, input().split(" "))

graph = [[] for _ in range(n)]

for i in range(m):
    (u,v) = map(int, input().split(" "))
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

# print(graph)


def dfs(node, par=-1):
    island = [node]
    count = 1
    for nei in graph[node]:
        if nei != par:
            res = dfs(nei, node)
            island += (res[0])
            count += (res)[1]

    return (island,count)

success = True
outs = []
    
c = []
aout = []

for i in range(n):
    if i in c:
        continue
    dfs_v = dfs(i)
    val =dfs_v[1]
    success = val % k == 0

    val = set(dfs_v[0])
    for o in val:
        c.append(o)
    ot = []
    for v in range(len(val)):
        ot.append(str((v%k)+1)) 
    
    aout.append(" ".join(ot))

    
if not success:
    print("impossible")
    exit()
    
print(" ".join(aout))
    



