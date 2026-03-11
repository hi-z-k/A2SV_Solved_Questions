n,k = list(map(int,input("").split()))
nums = list(map(int,input("").split()))

nums.sort()

diffs = []

for i in range(0,len(nums)-1):
    start,end = nums[i:i+2]
    diffs.append(end-start)

diffs.sort(reverse=True)
diff_reduce = sum(diffs[:k-1])
range_diff = nums[-1] - nums[0]

print(range_diff - diff_reduce)