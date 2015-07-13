import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return nums[0]
        if n == 1:
            return nums[0]
        A = {}
        for length in range(1, n+1):
            for i in range(n-length+1):
                if length == 1:
                    A[(i,length)] = nums[i]
                else:
                    A[(i,length)] = max( [A[(i,l)]*A[(i+l, length-l)] for l in range(1,length)] )
            print i, length, A
            pdb.set_trace()
        return A[(i,n)]


S = Solution()
test = [2,3,-2,4]
print S.maxProduct(test)
