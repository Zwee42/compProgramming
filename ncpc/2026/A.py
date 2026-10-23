
arr = {}
for i in range (ord("A"), ord("Z")):
    arr[chr(i)] = 0

rights = 0
points = 0

done = []

while(True):
    inp = input().split(" ")
    t = int(inp[0])
    if(t == -1):
        break
    question = inp[1]
    corr = inp[2]
        
    if question in done:
        continue
         
    if(corr == "wrong"):
        arr[question] += 1
    else:
        points += t + 20 * arr[question]
        done.append(question)
        
print(f"{len(done)} {points}")

    