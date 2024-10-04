class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase and remove spaces
        s = s.lower().replace(" ", "")
        # Remove non-alphanumeric characters
        s = ''.join(char for char in s if char.isalnum())

        # Check if the cleaned string is equal to its reverse
        return s == s[::-1]