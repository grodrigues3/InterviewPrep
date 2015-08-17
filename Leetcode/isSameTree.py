"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    
    def isSameTree(self, p ,q):
        return self.isSameTreeIter(p,q)
    
    def isSameTreeRecur(self, p, q):
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (q is None and p is not None):
            return False

        if(p.val == q.val):
            return self.isSameTreeRecur(p.right, q.right) and self.isSameTree(p.left, q.left)
        else:
            return False
            
    def isSameTreeIter(self, p,q):
        pQ = [p]
        qQ = [q]
        
        while pQ or qQ:
            if not pQ or not qQ:
                return False
            pCur = pQ.pop(0)
            qCur = qQ.pop(0)
            
            if pCur is None and qCur is None:
                continue
            elif pCur is None or qCur is None:
                return False
            
            if pCur.val != qCur.val:
                return False
                
            pQ += pCur.left,
            pQ += pCur.right,
            qQ += qCur.left,
            qQ += qCur.right,
            
        return True
                
