"""
Problem: Convert the Temperature
Platform: Leetcode
Link: https://leetcode.com/problems/convert-the-temperature/description/
Description: converting celsius to different temp scale
Difficulty: Easy
Complexity: O(1) Time | O(1) Space
"""

class UniversalSolver:
    def solve(self, *args):
        celsius = int(args[0])
        fahrenheit = lambda c: (c * 1.8)+32
        kelvin = lambda c: c + 273.15
        return [kelvin(celsius), fahrenheit(celsius)]
    
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