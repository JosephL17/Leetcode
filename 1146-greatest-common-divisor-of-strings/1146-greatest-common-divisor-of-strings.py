class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1):
            str1, str2 = str2, str1

        if str1 + str2 != str2 + str1:
            return ''

        greatest_Common_divisor = gcd(len(str1), len(str2))
        return str2[:greatest_Common_divisor]