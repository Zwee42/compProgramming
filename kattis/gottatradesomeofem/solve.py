n, m, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())  
    adj[a].append(b)
    adj[b].append(a)

# import sysg

# input_data = sys.stdin.read().split()
# if not input_data:
#   sys.exit(0)

# n = int(input_data[0])
# m = int(input_data[1])
# k = int(input_data[2])

# adj = [[] for _ in range(n + 1)]
# idx = 3
# for _ in range(m):
#   a = int(input_data[idx])
#   b = int(input_data[idx + 1])
#   idx += 2
#   adj[a].append(b)
#   adj[b].append(a)


visited = [False] * (n + 1)
ans = [0] * (n + 1)



for start in range(1, n + 1):
    if not visited[start]:
        component = []
        stack = [start]
        visited[start] = True
        
        while stack:
            node = stack.pop()
            component.append(node)
            
            for v in adj[node]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        if len(component) < k:
            print("impossible")
            exit()
                           
        for i, kid in enumerate(component):
            ans[kid] = (i % k) + 1

print(*ans[1:])