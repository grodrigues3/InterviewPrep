"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        return self.helper(l1, l2, 0)
    
    def helper(self, l1, l2, carry):
        if not l1 and not l2:
            if carry == 0:
                return
            return ListNode(1)
        elif not l1:
            return self.helper(l2, ListNode(carry), 0)
        if not l2:
            return self.helper(l1, ListNode(carry), 0)

        new = l1.val + l2.val + carry
        node = ListNode(new%10)
        node.next = self.helper(l1.next, l2.next, new/10)
        return node
