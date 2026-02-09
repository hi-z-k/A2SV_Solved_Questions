"""
Problem: Array Subset of another array
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
Description: Check whether array b is a subset of array a.
Difficulty: Easy
Complexity: O(n + m) Time | O(n + m) Space
"""

from collections import Counter

class UniversalSolver:
    def solve(self, a, b):
        return Counter(b) <= Counter(a)
    
    @staticmethod
    def fetch():
        try:
            line1 = input().strip()
            line2 = input().strip()
            if not line1 or not line2:
                return None
            a = list(map(int, line1.split()))
            b = list(map(int, line2.split()))
            return a, b
        except EOFError:
            return None
    
    @staticmethod
    def output(result):
        if result is True:
            print("Yes")
        elif result is False:
            print("No")


def main():
    data = UniversalSolver.fetch()
    
    if data:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()