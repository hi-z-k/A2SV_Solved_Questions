from collections import defaultdict
def longestGood(k, nums)->list[int]:
    values = set()
    i = 0
    longest = [1,1]
    count = defaultdict(int)
    for j in range(len(nums)):
        values.add(nums[j])
        count[nums[j]] += 1
        while len(values) > k:
            count[nums[i]] -= 1
            if not count[nums[i]]:
                values.remove(nums[i])
            i += 1
        prev = longest[1] - longest[0]
        curr = j - i
        if curr > prev:
            longest = [i+1, j+1]
    return longest

import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    # The user will provide the implementation of longestGood
    l, r = longestGood(k, nums)

    # Output 1‑based indices as required by the problem
    sys.stdout.write(f"{l} {r}")

if __name__ == "__main__":
    solve()