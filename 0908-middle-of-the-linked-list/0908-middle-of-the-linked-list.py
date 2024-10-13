# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # Initialize two pointers, both starting at the head of the list
        slow, fast = head, head

        # Traverse the list as long as fast and fast.next are not None
        # This ensures we do not run into a null reference
        while fast and fast.next:
            # Move the slow pointer one step forward
            slow = slow.next
            
            # Move the fast pointer two steps forward
            fast = fast.next.next
            
        # When fast reaches the end, slow will be at the middle
        return slow