# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast = curr
        while curr:
            for i in range(2):
                if fast.next:
                    fast = fast.next
                else:
                    return False
            if fast == curr:
                return True
            curr = curr.next
        return False