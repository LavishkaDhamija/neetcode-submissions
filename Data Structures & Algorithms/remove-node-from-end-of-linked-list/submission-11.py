# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
            
        first = head
        second = head

        for _ in range(n):
            second = second.next
        
        if second is None:
            return head.next

        while second.next != None:
            first = first.next
            second = second.next
        
        if head.next == None and n==1:
            head = None
            return head
        
        first.next = first.next.next

        return head
        