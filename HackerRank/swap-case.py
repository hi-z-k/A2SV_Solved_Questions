"""
Problem: SWAP case
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
Description: flip upercase with lowercase and viceversa
Difficulty: Easy
Complexity: O(n) Time | O(n) Space
"""

class UniversalSolver:
    @staticmethod
    def flip(letter):
        if not letter.isalpha():
            return letter
        ascii = ord(letter)
        return chr(ascii ^ 32)
        
    def solve(self, *args):
        flip = UniversalSolver.flip
        s = args[0]
        strList = []
        for l in s:
            strList.append(flip(l))
        return "".join(strList)
    
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