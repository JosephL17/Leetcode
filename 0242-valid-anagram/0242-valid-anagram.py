class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lower = s.lower()
        t_lower = t.lower()
        dict_of_s = {}
        dict_of_t = {}

        if len(s_lower) != len(t_lower):
            return False
        
        for letter in s_lower:
            if letter not in dict_of_s:
                dict_of_s[letter] = 1
            else:
                dict_of_s[letter] += 1

        for letter in t_lower:
            if letter not in dict_of_t:
                dict_of_t[letter] = 1
            else:
                dict_of_t[letter] += 1

        return dict_of_t == dict_of_s