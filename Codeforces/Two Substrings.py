"""
Problem: 
Platform: HackerRank, Leetcode, Codeforces
Link: 
Description:
Difficulty: 
Complexity: O() Time | O() Space
"""

class Solution:
    @staticmethod
    def check(string:str,phrase:str)-> int:
        return string.find(phrase)
    def solve(self, string):
        check = Solution.check
        alt = {
            "AB":"BA",
            "BA":"AB"
        }
        for n,m in alt.items():
            i = check(string,n)
            j = check(string[i+2:],m)
            if i != -1 and j != - 1:
                return 'YES'
        return 'NO'
    @staticmethod
    def fetch(count):
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
    data = Solution.fetch(1)
    if data:
        sol = Solution()
        result = sol.solve(*data)
        Solution.output(result)
        

if __name__ == "__main__":
    main()