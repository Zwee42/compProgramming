totin = input().split(" ")
n = int(totin[0])
m = int(totin[1])
k = int(totin[2])

# if (n % k != 0):
#     print("impossible")
#     exit()

if (k==1):
    print(" ".join(["1" for x in range(n)]))
    exit()
# groups
arr = []
    
for i in range(m):
    l = input().split(" ")
    a = l[0]
    b = l[1]
    hs = []
    at = False
    hsc = False
    c = False #contains
    sk = False
    for e in arr:
        if a in e and b in e:
            sk = True
            continue
        elif a in e:
            c = True
            if hs != []:
                hsc = True
                hs.extend(e)
                arr.remove(e)
                continue
            hs = e
        elif b in e:
            c = True
            if hs != []:
                hsc = True
                hs.extend(e)
                arr.remove(e)
                continue
            hs = e
            at = True

    # print(arr)

    if sk:
        continue
    elif not c:
        arr.append([a,b])
    elif not hsc:
        hs.append(a if at else b)
      
      
  
out = []
cg = 0
for e in arr:
    if len(e) < k:
        print("impossible")
        exit()
    for v in e:        
        out.append(str(cg+1))
        cg += 1
        cg = cg % k


if (len(out) < n and k > 1):
    print("impossible")
    exit()

print(" ".join(out))
    


