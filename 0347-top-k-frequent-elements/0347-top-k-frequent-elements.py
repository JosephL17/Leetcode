class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        # count the freq of elements
        counts = Counter(nums)
       
        # get the k most common elements
        most_freq = counts.most_common(k)

        return [element for element, _ in most_freq]