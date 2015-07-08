"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
__author__ = 'grodrigues'

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) <=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
    
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


