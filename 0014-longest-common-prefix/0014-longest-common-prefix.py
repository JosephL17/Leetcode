class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize an empty string to store the longest common prefix
        prefix = ''
        
        # Check if the list of strings is empty; if so, return an empty prefix
        if not strs:
            return prefix
        
        # Iterate over the characters of the first string in the list
        for i in range(len(strs[0])):
            # Get the current character to compare with others
            current_char = strs[0][i]
            
            # Compare this character with the same position in all other strings
            for word in strs[1:]:
                # If we reach the end of any string or the characters don't match
                if i >= len(word) or word[i] != current_char:
                    return prefix  # Return the current prefix if a mismatch is found
            
            # If all strings have the same character at the current index,
            # append it to the prefix
            prefix += current_char
        
        # Return the longest common prefix found
        return prefix