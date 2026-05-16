n,k,q = list(map(int,input("").split()))
max_temp = 200000
min_temp = 1
recipes = []
questions = []
for _ in range(n):
    l,r = list(map(int,input("").split()))
    recipes.append([l,r])
    min_temp = min(l, min_temp)
    max_temp = max(r, max_temp)
for _ in range(q):
    l,r = list(map(int,input("").split()))
    questions.append([l,r])

diff = [0]*(max_temp - min_temp + 2)
for l, r in recipes:
    diff[l-min_temp] += 1
    diff[r-min_temp + 1] -= 1
for i in range(1, len(diff)):
    diff[i] += diff[i-1]

accepted = [1 if x >= k else 0 for x in diff]
diff = [0] * (len(accepted) + 1)
for i in range(len(accepted)):
    diff[i+1] = diff[i] + accepted[i]

for a, b in questions:
    l = max(a, min_temp) - min_temp
    r = min(b, max_temp) - min_temp
    if l > r:
        print(0)
    else:
        print(diff[r+1] - diff[l])