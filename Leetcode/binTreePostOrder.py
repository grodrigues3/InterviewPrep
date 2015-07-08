"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None:
            return []
        trav = []
        return self.helper(root, trav)
        
        
        
    def helper(self, root, t):
        if root is None:
            return t
        self.helper(root.left, t)
        self.helper(root.right, t)
        t.append(root.val)
        return t
