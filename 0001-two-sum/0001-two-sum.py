class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty hashmap to store numbers and their indices
        h = {}
        
        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the complement value needed to reach the target
            value = target - num
            
            # Check if the value already exists in the hashmap
            if value in h:
                # If it exists, return the index of the complement and the current index
                return [h[value], i]
            
            # If the value does not exist, store the current number and its index in the hashmap
            h[num] = i