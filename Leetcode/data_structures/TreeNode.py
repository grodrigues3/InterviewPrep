class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
   

    def height(self):
        if self.left is None and self.right is None:
            return 1
        return max(self.left.height(), self.right.height()) + 1
    """ Come up with a pretty print later
    def __str__(self):
        pass
        h = self.height()
        toBuild = ""
        cur = self
        for i in range(h):
            toBuild += "\t"*(i-1) + cur.val
    """      
