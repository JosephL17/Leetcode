class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        for num in range(len(candies)):
            if candies[num] + extraCandies >= maxCandies:
                candies[num] = True
            else:
                 candies[num] = False
        return candies