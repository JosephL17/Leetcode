class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences_dict = {}
        count_dict = {}

        for num in arr:
            if num not in occurrences_dict:
                occurrences_dict[num] = 1
            else:
                occurrences_dict[num] += 1

        for num in occurrences_dict.values():
            if num not in count_dict:
                count_dict[num] = 1
            else: return False
        return True