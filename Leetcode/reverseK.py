#!/usr/bin/python
from data_structures.ListNode import ListNode
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k ==1:
            return head
        
        def reverseK(start):
            cur = start
            for i in range(k-1):
                cur = cur.next
                if cur is None:
                    return start
            
            prev = None
            cur = start
            i = 0
            while i < k:
                nn = cur.next
                cur.next = prev
                prev = cur
                cur = nn
                i += 1
            #start and end of the list
            if cur is None:
                return prev
            start.next = reverseK(cur)
            return prev
            
        return reverseK(head)



def test0(soln):
    head = ListNode(1)
    k = 1
    print "Original LL: {0}, K: {1}".format(head, k)
    print soln.reverseKGroup(head, k)

def test1(soln):
    head = ListNode(1)
    head.next = ListNode(2)
    k = 2
    print "Original LL: {0}, K: {1}".format(head, k)
    print soln.reverseKGroup(head, k)
    
def test2(soln):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    k = 2
    print "Original LL: {0}, K: {1}".format(head, k)
    print soln.reverseKGroup(head, k)

def test3(soln):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    k = 3
    print "Original LL: {0}, K: {1}".format(head, k)
    print soln.reverseKGroup(head, k)

if __name__ == "__main__":
    S = Solution()
    test0(S)
    test1(S)
    test2(S)
    test3(S)



