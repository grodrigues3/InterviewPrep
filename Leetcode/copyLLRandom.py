#Definition for singly-linked list with a random pointer.

import pdb
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    copied = {}
    #notFound = []
    def copyRandomList(self, head):
        if head == None:
            return
        if head in self.copied:
            return self.copied[head]
        h_prime = RandomListNode(head.label)
        self.copied[head] = h_prime
        h_prime.next = self.copyRandomList(head.next)
        h_prime.random = self.copyRandomList(head.random)
        return h_prime


t = RandomListNode(-1)

t.random = t

S = Solution()
t_pr = S.copyRandomList(t)
print t, t_pr
#print t_pr, t_pr.next, t_pr.random
