# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        # remove this element
        target = length - n + 1

    
        prev = None
        curr = head
        for i in range(1, target + 1):
            if i == target:
                if length == 1:
                    curr = None
                    return curr
                if target == 1:
                    curr = curr.next
                    return curr
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next
        return head
            
        





            