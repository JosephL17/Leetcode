class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer for the position of unique elements
        k = 0
        
        # Iterate through the nums array
        for i in range(len(nums)):
            # If we find a unique element or the first element
            if i == 0 or nums[i] != nums[i - 1]:
                # Place it in the next position of unique elements
                nums[k] = nums[i]
                # Move the unique elements pointer forward
                k += 1
        
        # Return the number of unique elements
        return k

        