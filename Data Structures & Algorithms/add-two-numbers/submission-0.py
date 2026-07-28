# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        head = None
        def addNode(v):
            nonlocal curr
            nonlocal head
            n = ListNode()
            n.val = v
            if curr is None:
                curr = n
                n.next = None
                head = curr
            else:
                curr.next = n
                n.next = None
                curr = n
        

        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            digit = total % 10
            carry = total // 10
            l1 = l1.next
            l2 = l2.next
            addNode(digit)
        
        while l1:
            total = l1.val + carry
            digit = total % 10
            carry = total // 10
            l1 = l1.next
            addNode(digit)
        
        while l2:
            total = l2.val + carry
            digit = total % 10
            carry = total // 10
            l2 = l2.next
            addNode(digit)
        
        if carry != 0:
            addNode(carry)

        return head
            


        