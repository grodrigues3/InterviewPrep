

class Node:
	def __init__(self, key, left=None, right=None, parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = None

	def setParent(self, par):
		self.parent = par
	def printMe(self):
		if self.left != None:
			self.left.printMe()
		print self.key
		if self.right !=None:
			self.right.printMe()
	
	def findMax(self):
		if self.right == None:
			return self 
		right = self.right
		while right.right != None:
			right = right.right
		return right

	def findMin(self):
		if self.left == None:
			return self
		left = self.left
		while left.left != None:
			left = left.left
		return left

	def findPred(self, val):
		pass
	
	def search(self,path=[], val=None):
		if self.key == val:
			return path+[], self
		elif val < self.key:
			if self.left  == None:
				return -1
			return self.left.search(path+['l'],val)
		elif val > self.key:
			if self.right == None:
				return -1
			return self.right.search(path+['r'],val)

	def findPred(self, val):
		if self.key == val:
			if self.left !=None:
				return self.left.findMax()
			else:
				par = self.parent
				while par.key > val:
					if par.parent != None:
						par = par.parent
					else:
						return -1
				return par

		elif val < self.key:
			return self.left.findPred( val)	
		elif val > self.key:
			return self.right.findPred( val)	

# Build the Tree		
four = Node(4)
five = Node(5,four)
one_pt_five = Node(1.5, None,None)
two = Node(2,one_pt_five)
one = Node(1,None,two)
root = Node(3, one, five)
one.setParent(root)
five.setParent(root)
two.setParent(one)
four.setParent(five)
one_pt_five.parent = two
#DO STUFF
root.printMe()
print '-'*20
print root.findMax().key
print 'finding max of four', four.findMax().key
print '-'*20
print root.findMin().key

print '-'*20
path, node = root.search(val=5)
print path
print node.key
path, node = root.search(val=2)
print path
print node.key
print root.search(val=-4)
print '-'*20

print root.findPred(3).key
print root.findPred(5).key
print root.findPred(2).key
print root.findPred(1.5).key
