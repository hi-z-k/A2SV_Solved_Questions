c = input("")
nums = list(map(int,input("").split(" ")))

nums.sort()
median_idx = (len(nums)-1)//2

print(nums[median_idx])