class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        # store value and index in hashmap as key/value
        for i, num in enumerate(nums):
            h[num] = i
        # loop through nums array to get the index we need for i
        for i, num in enumerate(nums):
        # create variable for desired value by subtracting target by current num in list
            value = target - num
            # as we loop through nums list, check if value is in hashmap and i doesnt equal j
            if value in h and h[value] != i:
                return [i, h[value]]