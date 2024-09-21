class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels:
                if s[right] in vowels:
                    s[left], s[right] = s[right], s[left]
                    right -= 1
                    left += 1
                else:
                    right -= 1
            else:
                left += 1
        
        return "".join(s)