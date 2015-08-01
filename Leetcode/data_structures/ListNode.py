# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        toWrite = ""
        cur = self
        while cur:
            toWrite += str(cur.val) + ", "
            cur = cur.next
        return toWrite[:-2]
