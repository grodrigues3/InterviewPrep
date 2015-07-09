"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
Do it O(n) time
    - a simple solution not meeting the above constraint would be to sort the list and then return the kth element from the end
"""
import random

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        
        #return sorted(nums)[-k] cheater solution
        n = len(nums)
        partInd = random.choice(range(n))
        part = nums[partInd]
        #swap em for easy partitioning
        nums[partInd], nums[0] = nums[0], nums[partInd]

        #because I'm lazy and don't want to partition in place
        smaller = []
        bigger = []        
        for i in range(1,len(nums)):
            if nums[i] >= part:
                bigger += nums[i],
            elif nums[i] < part:
                smaller += nums[i],
        
        nBigger = len(bigger)
        if nBigger == k-1:
            return part
        elif nBigger > k-1:
            return self.findKthLargest(bigger, k)
        else:
            return self.findKthLargest(smaller, k - nBigger - 1)
            
            
