# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    myMap = {}
    def kthSmallest(self, root, k):
        numSmaller = self.countNodes(root.left)
        if numSmaller == k -1:
            return root.val
        elif k > numSmaller + 1:
            return self.kthSmallest(root.right, k - numSmaller -1)
        else:
            return self.kthSmallest(root.left, k)
        
    def countNodes(self, root):
        if root is None:
            return 0
        if root in self.myMap:
            return self.myMap[root]
        numBefore = 1
        if root.left:
            numBefore += self.countNodes(root.left)
        if root.right:
            numBefore += self.countNodes(root.right)
            
        self.myMap[root] = numBefore
        return numBefore
