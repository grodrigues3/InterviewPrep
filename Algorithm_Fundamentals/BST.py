class BST:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def search(self, val):
        if self.val == val:
            return self
        elif val < self.val:
            return self.left.search(val) if self.left else None
        else:
            return self.right.search(val) if self.right else None

    def find_pred(self, val):
        node = self.search(val)
        if node.left:
            cur = node.left
            while cur.right:
                cur = cur.right
            return cur
        else:
            return None



    def insert(self, val):

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
                self.left.parent = self
        elif val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)
                self.right.parent = self
        else:
            if self.left:
                tmp = self.left
                self.left = BST(val)
                self.left.left = tmp
                self.left.parent = self
            else:
                self.left = BST(val)


    def remove(self, val):
        node = self.search(val)
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            if node.parent.right == node:
                node.parent.right = None
        elif node.left and node.right:
            print 'removing an internal node'
            pred = node.find_pred(node.val)
            node.val, pred.val = pred.val, node.val
            if pred.parent.left == pred:
                pred.parent.left = None
            else:
                pred.parent.right = None
        elif node.left:
            if node.parent:
                node.parent.left = node.left
            else:
                return node.left
        elif node.right:
            if node.parent:
                node.parent.right = node.right
            else:
                return node.right
        return self

    def pprint(self):
        
        def helper(root):
            q, q2 = [], []
            q += root,
            levels = []
            while q:
                levels.append([])
                while any(q):
                    cur = q.pop(0)
                    if cur:
                        levels[-1].append(cur.val)
                        q2 += cur.left,
                        q2 += cur.right, 
                    else:
                        levels[-1].append(None)
                if any(q2):
                    q,q2 = q2, [] 
            for level in levels:
                print level
        helper(self)

    def __str__(self):
        return str(self.val)

def setup():
    root = BST(2)
    root.insert(1)
    root.insert(3)
    root.insert(5)
    return root

def test_insert():
    root = setup()
    print [str(root.search(i)) for i in range(1,6)]
test_insert()
def test_remove():
    #one child
    root = setup()
    root = root.remove(3)
    root.pprint()
    print '-'*10
    #no children
    root = setup()
    root = root.remove(1)
    root.pprint()
    print '-'*10

    #remove root with one child
    root = setup()
    root = root.remove(1)
    root = root.remove(2)
    root.pprint()
    #remove two child root

test_remove()
print '-'*10
def test_remove_2():
    root = setup()
    root.pprint()
    nr = root.remove(2)
    nr.pprint()

test_remove_2()
