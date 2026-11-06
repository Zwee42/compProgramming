
import heapq

n, m = map(int, input().split())

saves = 0
ct = 0
e = []

schedule = []

for _ in range(0, n):
    
    v = list(map(int, input().split()))
    
    a = v[0]
    s = v[1]
    
    schedule.append((a, s))
    
schedule.sort()

d = 0

for v in schedule:
    a = v[0]
    s = v[1]
    
    ct = a
   
    ## Ränsa 
    while len(e) > 0 and ct - e[0] > m and ct- e[0] > 0:
        # if d: print(f"Event {e[0]} is now too old")
        # e.pop(0)
        heapq.heappop(e)


    if len(e) > 0 and ct - e[0] <= m and ct - e[0] >= 0:
        # if d: 
        #     print(f"Saved E: {e[0]} at ct: {ct}")
        saves += 1
        heapq.heappop(e)
        # e.pop(0)
     
     
    heapq.heappush(e, a+s)
    # e.append(a+s)
    # e.sort()
    
    # if d: print(f"CT: {ct}, Events: {e}")

# print(schedule)    
print(saves)
    
    
