# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
                return None
        if root == p or root == q:
                return root
        left = self.lowestCommonAncestor(root.left, p,q) #look for the p or q in the left subtree
        right = self.lowestCommonAncestor(root.right, p,q) #look for the p or q in the right subtree
        if left is not None and right is not None:
                return root
        if left is not None:
                return left
        else:
                return right
