"""
Problem: Python If-Else
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/py-if-else/problem
Description: Given an integer n, determine if it's weird or not based on specified conditions.
Difficulty: Easy
Complexity: O(1) Time | O(1) Space
"""

class Solver:
    def solve(self, *args):
        n = int(args[0])
        if n % 2 == 0 and (n in range(2,6) or n > 20):
            return 'Not Weird'
        else:
            return 'Weird'
    
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