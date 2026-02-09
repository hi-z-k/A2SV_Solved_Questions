"""
Problem: List Comprehensions
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
Description: Generate a list of all possible coordinates (i, j, k) where i+j+k != n.
Difficulty: Easy
Complexity: O(x*y*z) Time | O(x*y*z) Space
"""

class UniversalSolver:
    def solve(self, x, y, z, n):
        cuboid = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
        return cuboid
    
    @staticmethod
    def fetch(count=4):
        data = []
        for _ in range(count):
            line = input().strip()
            if line:
                data.append(int(line))
        return data
    
    @staticmethod
    def output(result):
        print(result)


def main():
    data = UniversalSolver.fetch(4)
    
    if len(data) == 4:
        solver = UniversalSolver()
        result = solver.solve(*data)
        UniversalSolver.output(result)


if __name__ == "__main__":
    main()