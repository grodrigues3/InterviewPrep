"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

"""
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        ind = 0
        n = len(s)
        for i,letter in enumerate(s):
            ind += (ord(letter)-64)*26**(n-i-1)
        return ind
