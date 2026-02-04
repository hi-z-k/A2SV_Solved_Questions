"""
Problem: string split and join
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
Description: splitting by space and joining by hypen
Difficulty: Easy
Complexity: O(n) Time | O(n) Space
"""

class UniversalSolver:
    def solve(self, *args):
        line = args[0]
        s = line.split(" ")
        result = "-".join(s)
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
    data = UniversalSolver.fetch(1)
    
    if data:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()