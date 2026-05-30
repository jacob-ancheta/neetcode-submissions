# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        def reverse(node):
            prev = None
            curr = node
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
            
        def midNode(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        
        mid = midNode(head)
        revHead = reverse(mid.next)
        mid.next = None
        curr = head
        while curr and revHead:
            temp = curr.next
            tempRev = revHead.next
            curr.next = revHead
            revHead.next = temp
            curr = temp
            revHead = tempRev
        if curr:
            curr.next = revHead
