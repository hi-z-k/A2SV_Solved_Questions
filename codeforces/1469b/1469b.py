def prefix(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
def maxPrefix(r, b):
    prefix(r)
    prefix(b)
    return max(max(*r, 0)+max(*b, 0), 0)


t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    print(maxPrefix(r, b))