n = input()
todo = (input().split(' '))
done = (input().split(' '))

for i in todo:
    if i not in done:
        print (i)
        break