def isBroken(string):
    fine = set()
    i = 0
    while i < len(string):
        j = i
        while j < len(string) and string[j] == string[i]:
            j += 1 
        length = j - i
        if length % 2:
            fine.add(string[i])
        i = j
    return "".join(sorted(list(fine)))

for _ in range(t):
    s = input()
    print(isBroken(s))