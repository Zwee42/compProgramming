
n = int(input())

odds = []
evens = []

to_be_popped = 0
should_pop = "none"

a = list(sorted(map(int, input().split())))

for i in range(n):
    if a[i]  % 2 == 0:
        evens.append(a[i])
    #     if len(odds) > 1:
    #         odds.pop()
    #     else:
    #         should_pop = "odd"
    #         to_be_popped += 1
    else:
        odds.append(a[i])
    #     if len(evens) > 1:
    #         evens.pop()
    #     else:
    #         should_pop = "even"
    #         to_be_popped += 1
    # if(to_be_popped > 1):
    #     if(should_pop == "even"):
    #         evens.pop()
    #     else:
    #         odds.pop()
    #     to_be_popped -= 1
    
can_pop = True
while(can_pop):
    
    
    
    
        
# if(len(evens) > len(odds)):
#     evens.pop()
# else:
#     odds.pop()

print("Even numbers:", evens)
print("Odd numbers:", odds)
# print("Difference:", diff)