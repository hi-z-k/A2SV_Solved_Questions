"""
Problem: Smallest Even Multiple
Platform: LeetCode
Link: https://leetcode.com/problems/smallest-even-multiple/
Description: Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
Difficulty: Easy
Complexity: O(1) Time | O(1) Space
"""

class Solver:
    def solve(self, *args):
        n = int(args[0])
        if n % 2 != 0:
            return 2 * n
        return n
    
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
    data = Solver.fetch(1)
    
    if data:
        solver = Solver()
        result = solver.solve(*data)
        Solver.output(result)


if __name__ == "__main__":
    main()