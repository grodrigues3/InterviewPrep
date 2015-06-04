"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        return self.isHappyHelper(n, {})
        #return self.isHappy_nostr(n)
    
    def isHappyHelper(self, n, prev):
        if n == 1:
            return True
        elif n not in prev:
            prev[n] = 1
        else:
            return False
            
        new = 0
        for char in str(n):
            new += int(char)**2
            
        return self.isHappyHelper(new, prev)
    
    def isHappy_nostr(self, n):
        prev = {}
        while True:
            agr = 0
            while(n > 0):
                agr += (n%10)**2
                n /=10
            
            if agr == 1:
                return True
            
            if agr in prev:
                return False
            prev[agr] = 1
            n = agr
        return self.isHappy(agr)
            
