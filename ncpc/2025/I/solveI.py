(n, m) = map(int, input().split(" "))

followers = []
followerCount = []

for i in range(n):
    followers.append(set())
    followerCount.append(0)



for i in range(m):
    (u, v) = map(int, input().split(" "))
    followers[u-1].add(v)
    
for i in range(n):
    cfollowers = followers[i]

    for j in cfollowers:
        followfollow = followers[j-1]
        if i+1 not in followfollow:
            followerCount[j-1] = followerCount[j-1] + 1

maxf = max(followerCount)
print(followerCount.index(maxf)+1, maxf)
#print(followers)
