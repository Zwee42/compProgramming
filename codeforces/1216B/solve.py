
n = int(input())
vals = list(map(int, input().split()))

sorted_vals = sorted(set(vals), reverse=False)

out = []

dura = 0

for i in range(len(sorted_vals)):
    indexes = [j for j, x in enumerate(vals) if x == sorted_vals[i]]
    out += indexes[::-1]


for i, out_i in enumerate(out[::-1]):
    val = (vals[out_i] * i) + 1
    dura += val

print(dura)
print(' '.join([str(x+1) for x in out[::-1]]))

