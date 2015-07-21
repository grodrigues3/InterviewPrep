from collections import deque
"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        return self.approach2(nums, k)
    
    def approach1(self, nums, k):    
        return nums and [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
    
    def approach2(self, nums, k):
        d = deque()
        outs = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] <= i - k:
                d.popleft()
            if i >= k-1:
                outs += nums[d[0]],
            
        return outs


if __name__ == "__main__":
    s = Solution()
    test = ([1,3,-1,-3,5,3,6,7], 3)
    expected = [3,3,5,5,6,7] 

    r = s.maxSlidingWindow(*test)
    print r
    assert r == expected
