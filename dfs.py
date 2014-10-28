#First create a tree to test on

class Node:
	def __init__(self,cargo, left, right):
		self.cargo = cargo
		self.right = right
		self.left = left

E=Node('E', None,None)
D =Node('D', None, None)
C = Node('C',None,None)
A = Node('A',C,D)
B = Node('B',C,E)
root = Node('root',A,B);
global explored
global toWrite
explored= []
toWrite = ""

def dfs(root):
	global explored
	global toWrite
	if root == None:
		return
	if root.cargo not in explored:
		explored += [root.cargo]
		toWrite += str(root.cargo)+","
	dfs(root.left)
	dfs(root.right)
	return toWrite
if __name__ == "__main__":
	dfs(root)
	print 'root,A,C,D,B,C,E'
	print toWrite
