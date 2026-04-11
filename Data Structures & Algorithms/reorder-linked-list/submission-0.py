# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:


    def reorderList(self, head: Optional[ListNode]) -> None:

        # step.1 取得 list 長度,並將慢指標指向中間節點
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = slow.next = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        temphead = head
        while prev:
            headnxt = temphead.next
            curnxt = prev.next

            temphead.next = prev
            prev.next = headnxt

            temphead = headnxt
            prev = curnxt

