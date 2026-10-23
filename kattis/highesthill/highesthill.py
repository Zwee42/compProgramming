
n = int(input())
22
rs = [int(i) for i in input().split(' ')]

s = True

r = []

for i in range(0,n-1):
    if(s):
        if(rs[i] >= rs[i+1]):
            continue
        else:
            s = False
            r.append(rs[i])
            continue
    if rs[i] != rs[i+1]:
        r.append(rs[i])
    if i == n-2 and r[-1] != rs[i+1]:
        r.append(rs[i+1])
    
s = True
n = len(r)  
v = []          

if len(r) == 0:
    print(0)
    exit()

# print(r)
            
for i in range(0,n-2):
    if(s):
        if(r[i] > r[i+1]):
            continue
        else:
            s = False
            v.append(r[i])
            
    if not (r[i] < r[i+1] < r[i+2] or r[i] > r[i+1] > r[i+2]): #and v[-1] != r[i]:        
        v.append(r[i+1])
if len(v) < 3 or v[-1] > v[-2]:
    v.append(r[-1])
    
# print(v)

h = 0
for i in range(1, len(v)-1, 2):
    h = min(v[i] - v[i-1], v[i] - v[i+1])
print(h)

