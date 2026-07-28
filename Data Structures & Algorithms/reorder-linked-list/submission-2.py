# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = None
        head1 = None
        def addNode(node):
            nonlocal curr
            nonlocal head1
            if curr == None:
                curr = node
                head1 = curr
            else:
                curr.next = node
                node.next = None
                curr = node

        def reverse_list(head):
            prev = None
            curr = head
            while curr != None:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if head.next is None:
            return

        fast = head
        slow = head
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        reversed_head = reverse_list(slow)

        while head and reversed_head:
            t1 = head
            t2 = reversed_head
            head = head.next
            reversed_head = reversed_head.next
            addNode(t1)
            addNode(t2)
            
        while head:
            t1 = head
            head = head.next
            addNode(t1)
        
        while reversed_head:
            t2 = reversed_head
            reversed_head = reversed_head.next
            addNode(t2)

        
            

        
        
        


        