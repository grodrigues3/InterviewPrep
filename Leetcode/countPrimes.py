"""
Count the number of prime numbers less than a non-negative number, n.
"""
__author__ = 'grodrigues'

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <=2:
            return 0
        maxFact = int(n**.5)+1
        primes = [1]*n
        primes[0] = primes[1] = False
        for i in range(2, maxFact):
            for j in range(i+i, n, i):
                primes[j] = False
                
        return sum(primes)
        
