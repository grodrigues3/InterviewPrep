# Definition for singly-linked list.
class ListNode:
     	def __init__(self, x, next):
        	self.val = x
	        self.next = next 

	def __cmp__(self, other):
		if other == None:
			return 1
		if self.val < other.val:
			return -1
		elif self.val == other.val:
			return 0
		else:
			return 1
	
	def __str__(self):
		if self.next != None:
			return str(self.val) +","+ self.next.__str__()
		else:
			return str(self.val)
	
	
class Solution:
	def sortList(self, head):
		sz = self.get_size(head)	
		print head,"\t",sz, 'the ll and its size'
		if sz == 1:
			return head
		current = head
		for i in range(sz/2-1):
			current = current.next
		right = current.next
		current.next = None
		left = head
		s_r = self.sortList(right)
		s_l = self.sortList(left)
		return self.merge_sorted(s_r, s_l)
		
			
	def get_size(self, head):
		if head == None:
			return 0
		else:
			total = 1
			current = head
			while current.next != None:
				total +=1
				current = current.next	
			return total
	def merge_sorted(self, one, two):
		head = ListNode(None, None)
		tail = head
		while self.get_size(one) != 0 or self.get_size(two) != 0:
			if self.get_size(one) == 0:
				tail.next = two
				break
			elif self.get_size(two) == 0:
				tail.next = one
				break
			if one.val <= two.val:
				tail.next = one
				tail = tail.next
				one = one.next
			else:
				tail.next = two
				tail = tail.next
				two = two.next
		head = head.next
		return head
	
	def reverse(self, node, nextNode):
		if nextNode == None:
			print 'in here'
			return node
		forwardNode = nextNode.next
		nextNode.next = node
		return self.reverse(nextNode, forwardNode)
		

vals = [5,3,6,2,1,4]
lenVal = len(vals)
myList = []
for i in range(len(vals)):
	current = lenVal - i-1
	if current != lenVal - 1:
		myList +=[ListNode(vals[current], myList[-1])]
	else:
		myList += [ListNode(vals[current],None)]
	

		
head = myList[-1]

Soln = Solution()
head = Soln.sortList(head)
print head
print "TRYING TO REVERSE"
print 'this is the head', head
hcopy = head
print head
rev = Soln.reverse(head, head.next)
hcopy.next = None
print rev
print '-'*30

print Soln.sortList({1})
