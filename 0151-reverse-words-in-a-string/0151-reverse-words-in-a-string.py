class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words, automatically handling multiple spaces
        reversed_str = s.split()
        
        # Join the reversed list of words with a single space
        return ' '.join(reversed_str[::-1])