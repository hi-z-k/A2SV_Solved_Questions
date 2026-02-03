"""
Problem Name: Arithmetic Operation
Platform: HackerRank
Difficulty: Easy
Link: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

Description:
computing basic math operations for two inputs
"""

import sys

class Solution:
    def solve(self, a, b):
        """
        Computing addition, subtraction & multiplication 
        for
        
        Args:
            a,b
        Returns:
            the computation result
        """
        add = a + b
        subt = a - b
        mult = a * b
        return [add, subt, mult]

def main():
    a = int(input())
    b = int(input())
    
    sol = Solution()
    results = sol.solve(a,b)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()