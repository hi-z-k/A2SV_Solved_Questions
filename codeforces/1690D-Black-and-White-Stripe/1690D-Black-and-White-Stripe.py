from collections import Counter
def blackWhite(k, stripe):
    count = Counter(stripe[:k])
    i = 0
    minFlip = count["W"]
    for i in range(k,len(stripe)):
        count[stripe[i-k]] -= 1
        count[stripe[i]] += 1
        minFlip = min(minFlip, count["W"])
    return minFlip

t = int(input())
for _ in range(t):
    n, k = list(map(int,input("").split()))
    stripe = list(input(""))
    print(blackWhite(k, stripe))