from itertools import combinations, permutations
from collections import deque

goal_state = "123-"

start = input() + input()
valid_moves = {0: [1,2], 1: [0,3], 2: [0,3], 3: [1,2]}

if start == goal_state:
    print(0)
    exit()

q = deque([(start, 0)])
seen = {start}

while q:
    cur, d  = q.popleft() 
    
    if cur == goal_state:
        print(d)
        exit()
    
    z = cur.index('-')
    
    for v in valid_moves[z]:
        n_state = list(cur)
        n_state[z], n_state[v] = n_state[v], n_state[z]
        
        nxt = "".join(n_state)
        
        if nxt not in seen:
            seen.add(nxt)
            q.append((nxt,d+1))
