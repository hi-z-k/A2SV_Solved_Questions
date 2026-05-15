def filpBits(a, b):
    equalCount = [False] * len(a)
    count = {'0': 0, '1': 0}
    
    for i in range(len(a)):
        count[a[i]] += 1
        if count['0'] == count['1']:
            equalCount[i] = True

    flipped = False
    
    for j in range(len(a) - 1, -1, -1):
        a_bit = a[j]
        if flipped:
            a_bit = '1' if a_bit == '0' else '0'
            
        if a_bit != b[j]:
            if not equalCount[j]:
                return "NO"
            flipped = not flipped
            
    return "YES"

t = int(input())
for _ in range(t):
    n = input()
    a = list(input().strip())
    b = list(input().strip())
    print(filpBits(a, b))