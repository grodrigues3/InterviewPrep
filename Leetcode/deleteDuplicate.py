"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

This is a simple two pointer problem that requires lookahead
"""
from data_structures.ListNode import ListNode


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            ne = cur.next
            while ne and ne.val == cur.val:
                ne = ne.next
            cur.next = ne
            cur = cur.next
        return head 



def setup_test(test):
    for i, val in enumerate(test):
        test[i] = ListNode(val)

    for i in range(len(test)-1):
        test[i].next = test[i+1]
    print "Test setup Complete..."
    print "\t", test[0]
    return test[0]

if __name__ == "__main__":
    S = Solution()
    test = [1,1,2,3]
    head = setup_test(test)
    new = S.deleteDuplicates(head)
    print "\t", new
    test2 = []
    for i in range(10):
        test2 += [i]*3
    test2 = setup_test(test2)
    trimmed = S.deleteDuplicates (test2)
    print "\t",trimmed
