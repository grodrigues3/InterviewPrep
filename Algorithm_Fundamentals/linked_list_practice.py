class node:
	def __init__(self, cargo, next = None):
		self.cargo = cargo
		self.next = next
	def print_list(self):
		print self.cargo
		if self.next != None:
			self.next.print_list()
	def reverse(self, next):
		if next == None:
			return self
		else:
			forward_next = next.next
			next.next = self
			return next.reverse(forward_next)

#TESTING 
D = node(12)
C = node(10,D)
B = node(8,C)
A = node(6,B)

A.print_list()
print "================"
rev = A.reverse(B)
A.next = None
rev.print_list()
