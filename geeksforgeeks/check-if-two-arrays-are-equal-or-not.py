"""
Problem: Check if two arrays are equal or not
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
Description: Two arrays are considered equal if they contain the same elements with the same frequencies.
Difficulty: Easy
Complexity: O(n) Time | O(n) Space
"""

from collections import Counter

class UniversalSolver:
    def solve(self, a, b):
        return Counter(a) == Counter(b)
    
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
        if result is not None:
            print(str(result).lower())


def main():
    data = UniversalSolver.fetch()
    
    if data:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()