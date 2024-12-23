from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = len(nums) // 2

        for key, val in counter.items():
            if val > majority:
                return key
        