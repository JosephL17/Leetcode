# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, both starting at the head of the list
        slow, fast = head, head

        # Traverse the list as long as fast and fast.next are not None
        # This ensures that we do not run into a null reference
        while fast and fast.next:
            # Move the slow pointer one step forward
            slow = slow.next
            
            # Move the fast pointer two steps forward
            fast = fast.next.next
            
            # Check if the slow pointer has caught up to the fast pointer
            if slow == fast:
                # If they meet, a cycle exists in the linked list
                return True
        
        # If we exit the loop, it means fast reached the end of the list
        # Therefore, there is no cycle
        return False