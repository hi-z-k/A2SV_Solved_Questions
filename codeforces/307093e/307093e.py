from collections import defaultdict

def countSegments(k, nums):
    left = 0
    freq = defaultdict(int)
    distinct = 0
    total = 0
    for right in range(len(nums)):
        freq[nums[right]] += 1
        if freq[nums[right]] == 1:
            distinct += 1
        while distinct > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                distinct -= 1
            left += 1
        total += right - left + 1
    return total

import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    
    result = countSegments(k, arr)
    sys.stdout.write(str(result))

if __name__ == "__main__":
    solve()