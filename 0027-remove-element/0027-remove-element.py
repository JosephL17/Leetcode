class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the position of elements not equal to val

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the current element to the k-th position
                k += 1  # Increment k for the next position

        return k  # Return the count of elements not equal to val