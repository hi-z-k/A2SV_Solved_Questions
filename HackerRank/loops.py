"""
Problem: Loops
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-loops/problem
Description: Read an integer n and print the square of each non-negative integer less than n.
Difficulty: Easy
Complexity: O(n) Time | O(n) Space
"""

class Solver:
    def solve(self, *args):
        n = int(args[0])
        result = []
        for i in range(n):
            result.append(i**2)
        return result
    
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