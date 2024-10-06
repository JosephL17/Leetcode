class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a Counter object for the first string 's'
        # Counter counts the occurrences of each character in 's'
        result1 = Counter(s)
        
        # Create a Counter object for the second string 't'
        # This counts the occurrences of each character in 't'
        result2 = Counter(t)

        # Compare the two Counter objects
        # If they are equal, it means both strings have the same characters
        # with the same frequency, thus they are anagrams
        return result1 == result2