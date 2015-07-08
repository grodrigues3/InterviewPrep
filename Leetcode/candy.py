"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        n = len(ratings)
        pieces = [1]*n #everyone starts with one
        for i, cur in enumerate(ratings):
            before = after = None
            if i != 0:
                before = ratings[i-1]
            if i != n-1:
                after = ratings[i+1]
            if before is not None and cur > before and pieces[i] <= pieces[i-1]:
                pieces[i] = pieces[i-1] + 1
            elif after is not None and cur > after and pieces[i] <= pieces[i+1]:
                pieces[i] = pieces[i+1] + 1
                
        for i in range(n-1,-1,-1):
            cur = ratings[i]
            before = after = None
            if i != 0:
                before = ratings[i-1]
            if i != n-1:
                after = ratings[i+1]
            if before is not None and cur > before and pieces[i] <= pieces[i-1]:
                pieces[i] = pieces[i-1] + 1
            elif after is not None and cur > after and pieces[i] <= pieces[i+1]:
                pieces[i] = pieces[i+1] + 1
        
        return sum(pieces)
        
            
