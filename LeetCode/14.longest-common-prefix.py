"""
Problem: Longest Common Prefix
Platform: LeetCode
Link: https://leetcode.com/problems/longest-common-prefix/
Description: Find the longest common prefix string amongst an array of strings.
Difficulty: Easy
Complexity: O(S) Time where S is the sum of all characters | O(1) Space
"""

class UniversalSolver:
    def solve(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix) and prefix:
                prefix = prefix[:-1]
        
        return prefix
    
    @staticmethod
    def fetch():
        data = []
        try:
            while True:
                line = input().strip()
                if not line:
                    break
                data.append(line)
        except EOFError:
            pass
        return data
    
    @staticmethod
    def output(result):
        if isinstance(result, list):
            for item in result:
                print(item)
        elif result is not None:
            print(result)


def main():
    data = UniversalSolver.fetch()
    
    if data:
        solver = UniversalSolver()
        result = solver.solve(data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()