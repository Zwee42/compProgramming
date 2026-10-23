niputs = int(input())

for line in range(niputs):
    text = input().split(" ")
    n = int(text[0])
    a = int(text[1]) # 5
    b = int(text[2])
    o = ""
    for i in range(n):
        o += chr((a + i) % b + 97)
    print (o)


