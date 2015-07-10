class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
   

    def height(self):
        if self.left is None and self.right is None:
            return 1
        return max(self.left.height(), self.right.height()) + 1

    def __str__(self):
        q = [self]
        explored = []

        while q:
            cur = q.pop(0)
            explored += cur.val,
            if cur.left:
                q += cur.left,
            if cur.right:
                q += cur.right,
        
        return str(explored)



