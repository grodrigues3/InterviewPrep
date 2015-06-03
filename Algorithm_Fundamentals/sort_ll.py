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
# @param head, a ListNode
# @retur a ListNode
	def sortList(self, head):
		pass

	def getSize(self, head):
		if head == None:
			return 0
		else:
			total = 1
			current = head
			while current.next != None:
				total +=1
				current = current.next	
			return total
	
	def partition(self, head, partition):
		
		self.swap(head,partition) #put the partition at the head
		head = partition
		next = partition.next
		boundary = partition.next
		while next != None:
			print next.val, partition.val
			raw_input()
			if next.val < partition.val:
				
				self.insertAfter(boundary, next)
				tmp = boundary.next 
				boundary.next = next
				next.next = tmp
				boundary = next
				head = next
				next = tmp
				print boundary
			else:
				next = next.next

		tmp = boundary.next
		boundary.next = head.next
		head.next = tmp
		head = boundary
		print head 

	def insertAfter(self, head, one, two):
		n = head	
		while n.next != two:
			n = n.next
		n.next = n.next.next
		temp = one.next
		one.next = two
		two.next = temp


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
print Soln.getSize(head)

Soln.insertAfter(head, myList[4], head.next.next.next)
print head
