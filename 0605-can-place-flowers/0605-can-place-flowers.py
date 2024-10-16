class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # iterate through flowerbed list
        for idx, plot in enumerate(flowerbed):
            # check to see if current plot has a seed in it
            if plot == 0:
                # checking to see if at the end of the flowerbed and if the previous plot is empty
                if idx == len(flowerbed) - 1 and flowerbed[idx - 1] == 0:
                    n -= 1
                    flowerbed[idx] = 1
                # checking to see if we're at the first plot in the flowerbed and if the next plot is empty
                elif idx == 0 and flowerbed[idx + 1] == 0:
                    n -= 1
                    flowerbed[idx] = 1
                # checking to see if the plots before and after are empty
                elif flowerbed[idx - 1] == 0 and flowerbed[idx + 1] == 0:
                    n -= 1
                    flowerbed[idx] = 1
        
        return (True if n <= 0 else False)