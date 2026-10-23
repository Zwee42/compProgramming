i = 0

curr = 1

cup = {}
cup[1] = 1
cup[2] = 2
cup[3] = 3

while(i < 5):
    
    f = int(input())
    t = int(input())

    v = cup[f]
    cup[f] = cup[t]
    cup[t] = v
    i+=1
    

print(cup[1])
    
    
    
    