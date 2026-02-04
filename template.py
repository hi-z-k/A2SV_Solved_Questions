"""
Problem: 
Platform: HackerRank, Leetcode, Codeforces
Link: 
Description:
Difficulty: 
Complexity: O() Time | O() Space
"""

class UniversalSolver:
    def solve(self, *args):
        return None
    
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