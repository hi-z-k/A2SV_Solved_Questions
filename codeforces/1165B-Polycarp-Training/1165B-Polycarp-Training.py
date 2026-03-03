contest = int(input(""))
problems = list(map(int,input("").split(" ")))

problems.sort()

curr_problems = 0
day = 1
for i,problem in enumerate(problems):
    if problem >= day:
        curr_problems += 1
        day += 1
    else:
        continue    

print(curr_problems)