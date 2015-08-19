"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        
        tot = 0
        first = True
        while first or tot >= 10:
            tot = 0
            while num > 0:
                tot += num % 10
                num /= 10
            num = tot
            first = False
        
        return tot
            
