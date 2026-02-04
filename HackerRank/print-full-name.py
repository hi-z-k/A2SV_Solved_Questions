"""
Problem: What's Your Name?
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/whats-your-name/problem
Description: Read firstname and lastname from input and print "Hello {firstname} {lastname}! You just delved into python."
Difficulty: Easy
Complexity: O(1) Time | O(1) Space
"""

class Solver:
    def solve(self, *args):
        first, last = args
        result = f"Hello {first} {last}! You just delved into python."
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
    data = Solver.fetch(2)
    
    if data:
        solver = Solver()
        result = solver.solve(*data)
        Solver.output(result)


if __name__ == "__main__":
    main()