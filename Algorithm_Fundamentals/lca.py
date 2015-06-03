
class Node:
	
	def __init__(self, value, left=None,right=None):
		self.left = left
		self.right = right
		self.value = value
	
	def setParent(self, parent):
		self.parent = parent
	
	

zero = Node(0)
eight = Node(8)
one = Node(1,zero,eight)
seven = Node(7)
four = Node(4)
two = Node(2,seven,four)
six = Node(6)
five = Node(5,six,two)
root = Node(3,five,one)



"""
				3
			/			\
			5			1
		/		\	/		\
		6		2	0		8

			    /	    \
			 7            4

"""

def lca(root, p,q):
	if root == None:
		return None
	if root.value == p or root.value == q:
		return root
	left = lca(root.left, p,q) #look for the p or q in the left subtree
	right = lca(root.right, p,q) #look for the p or q in the right subtree
	if left != None and right != None:
		return root
	if left != None:
		return left
	else:
		return right


def lca2(root, p,q):
	x,p_path = bfs(root,p,[])
	y,q_path = bfs(root,q,[])
	print [p.value for p in p_path]
	print [q.value for q in q_path]
	i = 0
	while 1:
		if i >= len(q_path) or i>=len(p_path):
			return p_path[i-1]
		if p_path[i].value != q_path[i].value :
			return p_path[i-1]
		i += 1

import copy
def bfs(root, val, path):
	path = copy.deepcopy(path)
	if root == None:
		return None,None
	path += [root]
	if root.value == val:
		return root, path
	l,p = bfs(root.left, val, path)
	if l:
		return l, p
	else:
		return bfs(root.right, val, path)
		

print lca(root, 4,8).value==3
print lca(root, 5,6).value==5
print lca(root, 7,4).value==2

node,path = bfs(root,4,[])
#print [node.value for node in path]
print lca2(root,4,8).value == 3
print lca2(root, 5,6).value==5
print lca2(root, 7,4).value==2
