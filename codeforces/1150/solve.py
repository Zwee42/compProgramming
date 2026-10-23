n = int(input())

board = [[] for i in range(n)]
in_use = [() for i in range(n**2)]

def is_valid(y,x):
    if y > n-1 or x > n-1:
        return False
    return (y,x) not in in_use and board[y][x] == '.'
    

for i in range(n):
    board[i] = [j for j in input()]


for y in range(n):
    for x in range(n):
        flag = True
        if is_valid(y,x):
            in_use.append((y,x))
            if x == 0 or x >= n-1 or y >= n-1:
                flag = False
            for r in range(x-1, x+2):
                if not is_valid(y+1,r):
                    flag = False
                else:
                    in_use.append((y+1,r))
            if not is_valid(y+2,x):
                flag = False
            else:
                in_use.append((y+2,x))
           
        if (not flag):
            print("NO")
            exit()     

# print(board)
print("YES")