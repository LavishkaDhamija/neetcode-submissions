"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = None
        head1 = None
        def addNode(value):
            nonlocal curr
            nonlocal head1
            n = Node(value,None)
            if curr is None:
                curr = n
                n.next = None
                head1 = curr
            else:
                curr.next = n
                n.next = None
                curr = n
            return n                
            
        pointer = head
        while pointer is not None:
            val = pointer.val
            copy = addNode(val)
            hashmap[pointer] = copy
            pointer = pointer.next

        while head is not None:
            copy = hashmap[head]
            if head.random is None:
                copy.random = None
            else:
                copy.random = hashmap[head.random]
            head = head.next
    
        return head1

        