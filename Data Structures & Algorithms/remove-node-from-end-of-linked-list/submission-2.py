# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        target, node, size = head, head, 0
        while node:
            node = node.next
            size += 1
        
        if size == n:
            return head.next
            
        for i in range(size - n):
            prev = target
            target = prev.next
            nxt = target.next
        
        prev.next = nxt
        return head

            


         