# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
INPUT:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

OUTPUT
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
