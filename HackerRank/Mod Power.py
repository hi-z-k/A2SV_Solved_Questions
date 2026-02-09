"""
Problem: Power - Mod Power
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-power-mod-power/problem
Description: Calculate a^b and a^b % m
Difficulty: Easy
Complexity: O(log b) Time | O(1) Space
"""

class UniversalSolver:
    def solve(self, a, b, m):
        a, b, m = int(a), int(b), int(m)
        res1 = pow(a, b)
        res2 = pow(a, b, m)
        return [res1, res2]
    
    @staticmethod
    def fetch(count=3):
        data = []
        for _ in range(count):
            line = input().strip()
            if line:
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
    data = UniversalSolver.fetch(3)
    
    if len(data) == 3:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()