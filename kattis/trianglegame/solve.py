
inp = input()
while inp != "$":
    sum = 0
    tria = []
    while inp != "*":

        a, b, c = map(int, inp.split())
        tria.append([a,b,c])
    
    flag = True
    edge = tria[0][0]
    t_i = 0
    while flag:

        for i in range(0,tria):
            if tria_i == i:
                continue

        #    a, b, c = tria[i]
            for val_i in tria[i]:
                if edge == val_i:
                    edge = val_i
                    t_i = i

        




            



print(sum)
