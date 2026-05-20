# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = []

        current = head
        while current:
            reversed.append(current.val)
            current = current.next
        reversed.reverse()

        if reversed:
            new_head = ListNode(reversed[0])
            current_node = new_head
            for i in range(1, len(reversed)):
                current_node.next = ListNode(reversed[i])
                current_node = current_node.next
                
            return new_head
            

