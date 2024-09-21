class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = len(word1) + len(word2)
        merge = ""

        for idx in range(size):
            if idx < len(word1):
                merge += word1[idx]
            if idx < len(word2):
                merge += word2[idx]
        return merge
            