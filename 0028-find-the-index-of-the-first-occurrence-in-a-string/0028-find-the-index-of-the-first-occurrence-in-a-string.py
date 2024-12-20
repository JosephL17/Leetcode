class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If the needle is an empty string, return 0
        if not needle:
            return 0
        
        # Lengths of the haystack and needle
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        # Iterate through the haystack
        for i in range(haystack_length - needle_length + 1):
            # Check if the substring matches the needle
            if haystack[i:i + needle_length] == needle:
                return i
        
        return -1