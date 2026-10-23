n = int(input())

a = input().split(" ")
ok = True
ac = 1
for c in a:
    # print (c)
    # print (ac)

    if c != "mumble" and int(c) != ac:
        ok = False
    ac+=1
    # print( )    

if ok:
    print("makes sense")
else:
    print("something is fishy")