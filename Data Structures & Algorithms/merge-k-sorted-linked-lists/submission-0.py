# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def addNode(node,head,curr):
            if curr is None:
                curr = node
                node.next = None
                head = curr
            else:
                curr.next = node
                node.next = None
                curr = node
            return head,curr

        def merge_two(l1,l2,head=None,curr=None):
            while l1 and l2:
                if l1.val == l2.val:
                    temp1 = l1
                    temp2 = l2
                    l1 = l1.next
                    l2 = l2.next
                    head,curr = addNode(temp1,head,curr)
                    head, curr = addNode(temp2,head,curr)     
                elif l1.val < l2.val:
                    temp1 = l1
                    l1 = l1.next
                    head,curr = addNode(temp1,head,curr)
                elif l1.val > l2.val:
                    temp2 = l2
                    l2 = l2.next
                    head,curr = addNode(temp2,head,curr)

            while l1:
                temp1 = l1
                l1 = l1.next
                head,curr = addNode(temp1,head,curr)
            while l2:
                temp2 = l2
                l2 = l2.next
                head,curr = addNode(temp2,head,curr)
            
            return head

        while len(lists) > 1:
            merged_lists = []
            for i in range(0,len(lists),2):
                if i + 1 < len(lists):
                    h = merge_two(lists[i],lists[i+1])
                else:
                    h = lists[i]
                merged_lists.append(h)
            lists = merged_lists
        
        if not lists:
            return None
        return lists[0]

