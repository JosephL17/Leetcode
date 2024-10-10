class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer x to a string to facilitate comparison
        # Compare the string representation of x to its reverse
        # str(x)[::-1] creates a reversed version of the string representation of x
        return str(x) == str(x)[::-1]