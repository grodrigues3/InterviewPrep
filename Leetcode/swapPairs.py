# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        for i in range(2):
            nn = cur.next
            cur.next = prev
            prev = cur
            cur = nn

        head.next = self.swapPairs(cur)
        return prev


"For tests, see reverseK.py, a slightly more generalized (complex) version of the same problem"
