"""
Problem: Union of Two Arrays
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
Description: Find the union of two arrays representing sets of integers.
Difficulty: Easy
Complexity: O(n + m) Time | O(n + m) Space
"""

class UniversalSolver:
    def solve(self, a, b):
        return set(a) | set(b)
    
    @staticmethod
    def fetch():
        try:
            a = list(map(int, input().split()))
            b = list(map(int, input().split()))
            return a, b
        except EOFError:
            return None
    
    @staticmethod
    def output(result):
        if result is not None:
            print(len(result))


def main():
    data = UniversalSolver.fetch()
    
    if data:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()