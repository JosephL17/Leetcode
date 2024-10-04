class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: l (left) starting from the beginning (index 0) 
        # and r (right) starting from the end (last index) of the 'numbers' list.
        l, r = 0, len(numbers) - 1

        # Start a loop that will continue as long as the left pointer is less than the right pointer.
        while l < r:
            # Calculate the current sum of the values at the left and right pointers.
            current_sum = numbers[l] + numbers[r]

            # If the current sum is greater than the target,
            # it means we need a smaller sum, so we move the right pointer left.
            if current_sum > target:
                r -= 1  # Decrease the right pointer to consider a smaller number.
            
            # If the current sum is less than the target,
            # we need a larger sum, so we move the left pointer right.
            elif current_sum < target:
                l += 1  # Increase the left pointer to consider a larger number.
            
            # If the current sum is exactly equal to the target,
            # we found the indices that sum up to the target.
            else:
                # Return the 1-based indices of the two numbers that add up to the target.
                return [l + 1, r + 1]