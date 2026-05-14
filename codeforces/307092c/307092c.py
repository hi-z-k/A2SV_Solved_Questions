c = input()
a = list(map(int,input("").split()))
b = list(map(int,input("").split()))

from collections import Counter

countB = Counter(b)

count = 0
for num in a:
    if num in countB:
        count += countB[num]

print(count)