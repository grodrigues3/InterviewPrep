"""
pathSum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, mysum):
        if not root:
            return []
        solutions = []
        stack = [root]
        path = [root.val]
        
        def dfs(tot):
            cur = stack.pop()
            tot += cur.val
            if cur.left is None and cur.right is None:
                if tot == mysum:
                    solutions.append(path[:])
                path.pop()
                #tot -= cur.val
            else:
                #not a leaf
                if cur.left:
                    stack.append(cur.left)
                    path.append(cur.left.val)
                    dfs(tot)
                if cur.right:
                    stack.append(cur.right)
                    path.append(cur.right.val)
                    dfs(tot)
                path.pop() #pop internal nodes
            
        dfs(0)   
        return solutions
    

        
