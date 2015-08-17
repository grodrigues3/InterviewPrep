"""
Symmetric Tree Total Accepted: 66661 Total Submissions: 210965 My Submissions Question Solution 
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root or (root.left is None and root.right is None):
            return True
        qL = [root.left]
        qR = [root.right]
        
        while qL or qR:
            curL = qL.pop(0)
            curR = qR.pop(0)
            if curR is None and curL is None:
                continue
            elif curR is None or curL is None:
                return False
            if curL.val != curR.val:
                return False
            qL += curL.left,
            qL += curL.right,    
            qR += curR.right,
            qR += curR.left,
            
        return True

if __name__ == "__main__":
    from data_structures.TreeNode import TreeNode
    
    threeL = TreeNode(3)
    threeR = TreeNode(3)
    fourL = TreeNode(4)
    fourR = TreeNode(4)
    twoL = TreeNode(2)
    twoR = TreeNode(2)
    root = TreeNode(1)

    root.left = twoL
    root.right = twoR
    twoL.left = threeL
    twoR.right = threeR
    twoL.right = fourR
    twoR.left = fourL
    
    S = Solution()
    print S.isSymmetric(root) #example from comments above
    
    twoR.right, twoR.left = twoR.left, twoR.right #swap two nodes and...
    print S.isSymmetric(root) #as is above
