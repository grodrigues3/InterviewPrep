"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)

        A = [ [0]*(m+1) for k in range(n+1)]
        
        for j in range(n+1):
            A[j][0] = j 
        
        
        for i in range(m+1):
            A[0][i] = i 
        
        for row in range(1, n+1):
            for col in range(1, m+1):
                A[row][col] = min(
                        A[row-1][col-1] + int(word1[row-1] != word2[col-1]),
                        A[row-1][col] + 1,
                        A[row][col-1] +1 )
                        
        return A[-1][-1]


def perform_tests(tests):
    S = Solution() 
    for w1, w2, dist in tests:
        found = S.minDistance(w1,w2)
        print "Word1: {0:>10} Word2: {1:>10} True Distance: {2:>10} Calculated Distance: {3:>10}". format(w1, w2, dist, found)
        assert dist == found


if __name__ == "__main__":
    t1 = 'cat', 'mat', 1
    t2 = 'cat', 'mate', 2
    t3 = 'garrett', 'carrot', 3

    perform_tests([t1,t2,t3])
