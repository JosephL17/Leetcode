class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Initialize a variable 'left' to track the position for the next non-zero element
        left = 0 

        # Iterate through each index 'i' in the range of the length of the list 'nums'
        for i in range(len(nums)):
            # Check if the current element at index 'i' is not zero
            if nums[i] != 0:
                # Swap the current element 'nums[i]' with the element at the 'left' index
                # This moves the non-zero element to the front of the list
                nums[i], nums[left] = nums[left], nums[i]
                
                # Increment 'left' to move to the next position for non-zero elements
                left += 1

        # Return the modified list 'nums', which now has all non-zero elements at the front
        return nums