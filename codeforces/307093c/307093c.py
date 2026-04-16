def atMost(nums,s):
    i = 0
    total = 0
    count = 0
    for j in range(len(nums)):
        total += nums[j]
        while total > s:
            total -= nums[i]
            i += 1
        count += j - i + 1
    return count


n,s = list(map(int,input("").split()))
nums = list(map(int,input("").split()))


print(atMost(nums,s))