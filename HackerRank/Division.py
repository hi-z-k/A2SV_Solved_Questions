"""
Problem Name: Division
Platform: HackerRank
Difficulty: Easy 
Link: https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

Description:
    division of two numbers(integer div/ float div)
"""


class Solution:
    @staticmethod
    def solve(a,b):
        """
        Two types of division
        
        Args:
            a,b: number input
        Returns:
            division of two numbers
        """
        # TODO: Implement solution
        return (a//b, a/b)


def main():
    a = int(input())
    b = int(input())
    
    sol = Solution()
    results = sol.solve(a,b)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()