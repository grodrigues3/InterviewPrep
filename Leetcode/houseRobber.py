"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

See Also: Weighted Independent Set
"""
__author__ = 'grodrigues'
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        
        #weighted independent set problem 
        n = len(num)
        if n == 0:
            return 0
        
        A = {0:0, 1: num[0] }
        if n == 1:
            return A[1]
            
        for j in range(2, n+1):
            A[j] = max( num[j-1]+A[j-2], A[j-1])
        
        return A[n]
