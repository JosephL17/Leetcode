class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        int_dict = {}

        for num in nums:
            if num not in int_dict:
                int_dict[num] = 1
            else:
                return True
        return False
        