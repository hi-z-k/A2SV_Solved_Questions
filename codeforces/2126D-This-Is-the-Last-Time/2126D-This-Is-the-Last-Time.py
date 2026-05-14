for _ in range(int(input())):
    test = []
    n,k = list(map(int,input("").split()))
    for _ in range(n):
        data = list(map(int,input("").split()))
        test.append(data)
    test.sort(key= lambda x: (x[0],-x[2]))
    maximum = k
    for l,r,real in test:
        if l <= maximum <= r and real > maximum:
            maximum = real
    print(maximum)