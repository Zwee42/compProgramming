istr = input()

l = istr.split("()")[0]
r = istr.split("()")[1]

print("correct" if len(l) == len(r) else "fix")
 