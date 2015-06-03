import dfs
X = range(15)

"""
				7
			/  			\
			3			11
		/		\	/		\
		1		5	9		13
	0		2  4       6 	810	12		14
		

"""
class Node:
	def __init__(self,cargo,left, right):
		self.cargo = cargo
		self.left = left
		self.right = right

def create_binary_tree(array):
	length = len(array)
	half = length/2
	if half > 0:
		left = create_binary_tree(array[0:half])
	else: 
		left = None
	if len(array) - (half+1) > 0:
		right = create_binary_tree(array[half+1:])
	else: 
		right = None
	root = Node(str(array[half]),left,right)
	return root
global toWrite
root = create_binary_tree(X)
X = dfs.dfs(root)
print X
