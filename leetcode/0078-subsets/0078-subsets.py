class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        path = []
        path_already = set()
        ans_already = set()
        def backtrack():
            if len(path) == len(nums):
                return
            for num in nums:
                if num in path_already:
                    continue
                path.append(num)
                path_already.add(num)
                backtrack()
                h = hash(tuple(sorted(path)))
                if h not in ans_already:
                    ans.append(path[:])
                    ans_already.add(h)
                path.pop()
                path_already.remove(num)
        backtrack()
        return ans