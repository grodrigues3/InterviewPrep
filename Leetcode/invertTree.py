from data_structures.TreeNode import TreeNode

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


def create_example():
    root = TreeNode(4)
    two = TreeNode(2)
    sev = TreeNode(7)
    one = TreeNode(1)
    thr = TreeNode(3)
    six = TreeNode(6)
    nin = TreeNode(9)

    root.left = two
    root.right = sev
    two.left = one
    two.right = thr
    sev.left = six
    sev.right = nin
    return root

if __name__ == "__main__":
    root = create_example()
    print root
    S = Solution()
    inverted =  S.invertTree(root)
    print inverted

