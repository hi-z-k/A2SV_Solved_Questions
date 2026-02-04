"""
Problem: Palindrome Number
Platform: Leetcode
Link: https://leetcode.com/problems/palindrome-number/description/
Description: check if a number is equal to itself when reversed
Difficulty: Easy
Complexity: O(n) Time | O(i) Space
"""

class UniversalSolver:
    def solve(self, *args):
        num = args[0]
        i = 0
        j = len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
        return True
    
    @staticmethod
    def fetch(count=1):
        data = []
        for _ in range(count):
            line = input().strip()
            data.append(line)
        return data
    
    @staticmethod
    def output(result):
        if isinstance(result, list):
            for item in result:
                print(item)
        elif result is not None:
            print(result)


def main():
    data = UniversalSolver.fetch(1)
    
    if data:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()