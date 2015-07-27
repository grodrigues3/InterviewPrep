"""
Given a linked list, determine if it has a cycle in it.

Follow up:
    Can you solve it without using extra space?
    In linear time.

Solution: Floyd's Tortoise and Hare Algorithm
"""
from data_structures.ListNode import ListNode
__author__ = 'grodrigues'



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

def test_1():
    myList = []
    for i in range(10):
        myList += ListNode(i),

    for i in range(9):
        myList[i].next = myList[i+1]

    return myList[0]


if __name__ == "__main__":
    t1 = test_1()
    S = Solution()
    print S.hasCycle(t1)

    cur = t1
    while cur.next:
        cur = cur.next

    cur.next = t1

    print S.hasCycle(t1)



