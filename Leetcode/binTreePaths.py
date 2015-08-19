"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        stack = [root]
        self.solutions = []
        path = []
        
        def dfs():
            if stack is None:
                return
            cur = stack.pop()
            path.append(str(cur.val))
            if cur.left is None and cur.right is None:
                self.solutions += [ "->".join(path[:]) ]
                path.pop()
            else:
                if cur.left:
                    stack.append(cur.left)
                    dfs()
                if cur.right:
                    stack.append(cur.right)
                    dfs()
                path.pop()
            
        dfs()
        return self.solutions
