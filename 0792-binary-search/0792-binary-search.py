class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left pointer to the start of the list
        l = 0
        # Initialize the right pointer to the end of the list
        r = len(nums) - 1
        
        # Continue the search while the left pointer is less than or equal to the right pointer
        while l <= r:
            # Calculate the middle index
            m = (l + r) // 2
            
            # Check if the middle element is the target
            if nums[m] == target:
                return m  # Target found, return the index
            
            # If the middle element is less than the target, ignore the left half
            if nums[m] < target:
                l = m + 1  # Move the left pointer to the right of the middle element
            else:
                # If the middle element is greater than the target, ignore the right half
                r = m - 1  # Move the right pointer to the left of the middle element
        
        # If the target is not found in the list, return -1
        return -1