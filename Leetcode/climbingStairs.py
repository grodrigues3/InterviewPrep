"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Spoiler: This reduces to fibonacci
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        f0 = f1 = 1
        for i in range(2, n+1):
            f0,f1 = f1, f0+f1
        
        return f1
        
