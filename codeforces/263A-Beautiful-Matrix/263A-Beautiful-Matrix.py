matrix = []
for _ in range(5):
    row = list(map(int,input("").split()))
    matrix.append(row)

loc = []
for i,row in enumerate(matrix):
    for j,num in enumerate(row):
        if num == 1:
            loc = [i+1,j+1]
x,y = loc

steps = abs(x-3) + abs(y-3)
print(steps)