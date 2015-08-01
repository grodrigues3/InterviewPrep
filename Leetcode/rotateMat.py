class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix) - 1
        if n <= 0:
            return
        sq = int(n**(.5))
        for i in range(sq):
            for j in range(sq):
                print i,j
                print matrix[i][j], matrix[i][n-j], matrix[n-i][n-j], matrix[n-i][j]
                print 'to'
                print matrix[i][n-j], matrix[n-i][n-j], matrix[n-i][j], matrix[i][j]
                matrix[i][j], matrix[i][n-j], matrix[n-i][n-j], matrix[n-i][j] = \
                    matrix[n-i][j], matrix[i][j], matrix[i][n-j], matrix[n-i][n-j] 
                raw_input("hello world") 

S = Solution()
test = [ [1,2], [3,4]]
print test
S.rotate(test)
print test
