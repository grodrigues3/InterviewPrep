class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):

        e = {}
        for thing in nums:
            if thing in e:
                return True
            else:
                e[thing] = 1
        return False
        
