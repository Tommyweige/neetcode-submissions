# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2, l1val, l2val = l1, l2, 0, 0
        count = 1
        while node1:
            l1val += node1.val * count
            count *= 10
            node1 = node1.next
        count = 1

        while node2:
            l2val += node2.val * count
            count *= 10
            node2 = node2.next
        
        total = l1val + l2val
        node = head = ListNode(total % 10)
        total //= 10      
        while total: 
            node.next = ListNode(total%10)
            node = node.next
            total //= 10
        return head

            