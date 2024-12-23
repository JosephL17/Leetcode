from collections import Counter  # Import the Counter class from the collections module

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a Counter object, which counts the occurrences of each element in nums
        counter = Counter(nums)
        
        # Calculate the majority count, which is half the length of the list (integer division)
        # The majority element should appear more than len(nums) // 2 times
        majority = len(nums) // 2  

        # Iterate through each key-value pair (element, count) in the counter dictionary
        for key, val in counter.items():
            # If the count of the current element is greater than the majority count
            # This means the current element is the majority element
            if val > majority:
                return key  # Return the majority element
        