class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the low and high pointers. These represent the range of indices
        # in the list that we will be searching through.
        low = 0  # Start with the first index of the list.
        high = len(nums) - 1  # Start with the last index of the list.

        # We continue searching as long as low is less than or equal to high
        while low <= high:
            # Find the middle index by averaging low and high.
            mid = (low + high) // 2

            # Check if the middle element is equal to the target.
            if nums[mid] == target:
                # If it is, return the current middle index, because we've found the target.
                return mid

            # If the middle element is greater than the target, then the target must be
            # in the left half of the list, so we move the high pointer to the left of mid.
            if nums[mid] > target:
                high = mid - 1  # Move the high pointer to the left of mid.

            # If the middle element is less than the target, then the target must be
            # in the right half of the list, so we move the low pointer to the right of mid.
            else:
                low = mid + 1  # Move the low pointer to the right of mid.

        # If we exit the loop, it means we didn't find the target in the list.
        # The low pointer will now be at the correct index where the target should be inserted.
        return low