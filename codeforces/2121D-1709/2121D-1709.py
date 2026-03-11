def numK(num1, num2):
    n = len(num1)
    state = []
    
    while True:
        changed = False
        
        for i in range(n):
            for j in range(n - 1):
                if num1[j] > num1[j+1]:
                    num1[j], num1[j+1] = num1[j+1], num1[j]
                    state.append((1, j + 1))
                    changed = True
        
        for i in range(n):
            for j in range(n - 1):
                if num2[j] > num2[j+1]:
                    num2[j], num2[j+1] = num2[j+1], num2[j]
                    state.append((2, j + 1))
                    changed = True
        
        for i in range(n):
            if num1[i] > num2[i]:
                num1[i], num2[i] = num2[i], num1[i]
                state.append((3, i + 1))
                changed = True
        
        if not changed:
            break
            
    return state

for a,b in tests:
    output = numK(a, b)
    print(len(output))
    for state, index in output:
        print(f"{state} {index}")