"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        self.make_flat(root)
    
    def make_flat(self, root):
        #flatten the left tree and return a ptr to it
        #flatten the right and return a ptr to it
        if not root:
            return
        rl = root.left
        rr = root.right
        if rl is None and rr is None:
            #leaf's are already flat
            return root
        lf = self.make_flat(root.left)
        rf = self.make_flat(root.right)
        root.left= None
        if lf:
            root.right = lf
            if rf:
                s = lf
                #step down the left subtree
                while s.right is not None:
                    s = s.right
                s.right = rf
        elif rf:
            # no left subtree so just point root's right subtree to flattened
            # right tree
            root.right = rf
        
        return root
