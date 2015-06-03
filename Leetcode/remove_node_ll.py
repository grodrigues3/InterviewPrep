"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        
        m1 = prev = ListNode(-1)
        prev.next = head
        cur = head
        while cur:
            if cur.val == val:
                #don't update prev
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return m1.next
        
