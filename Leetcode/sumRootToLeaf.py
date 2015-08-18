"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root:
            return 0
        stack = [root]
        path = [root.val]

        def dfs(tot):
            cur = stack.pop()
            if cur.left is None and cur.right is None:
                n = len(path)
                for i, val in enumerate(path):
                    tot += 10**(n-i-1)*val
                path.pop()
                return tot
            else:
                #not a leaf
                if cur.left:
                    stack.append(cur.left)
                    path.append(cur.left.val)
                    tot = dfs(tot)
                if cur.right:
                    stack.append(cur.right)
                    path.append(cur.right.val)
                    tot = dfs(tot)
                path.pop() #pop internal nodes
                return tot
            
        tot = dfs(0)   
        return tot
    
