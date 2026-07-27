# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        curr = None
        head = None
        def addNode(node):
            nonlocal curr
            nonlocal head
            if curr is None:
                curr = node
                head = curr
            else:
                curr.next = node
                node.next = None
                curr = node

        while l1 and l2:
            if l1.val == l2.val:
                temp1 = l1
                temp2 = l2
                l1 = l1.next
                l2 = l2.next
                addNode(temp1)
                addNode(temp2)
            elif l1.val < l2.val:
                temp1 = l1
                l1 = l1.next
                addNode(temp1)
            elif l1.val > l2.val:
                temp2 = l2
                l2 = l2.next
                addNode(temp2)
        
        while l1:
            temp1 = l1
            l1 = l1.next
            addNode(temp1)
        
        while l2:
            temp2 = l2
            l2 = l2.next
            addNode(temp2)
        
        return head
