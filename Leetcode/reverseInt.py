"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flip = False
        if x < 0:
            x = -x
            flip = True
        numDigs = 1
        while x / 10**numDigs > 0:
            numDigs += 1
        
        newNum = 0
        for i in range(numDigs):
            orig_dig = x/(10**i) % 10
            newNum += orig_dig * 10**(numDigs-i-1)
        if newNum > 2**31 -1:
            return 0
        if flip:
            return -newNum
        return newNum
