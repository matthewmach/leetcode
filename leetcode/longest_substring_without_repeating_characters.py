"""
- 2 pointers, have dict of pointers
    - move the pointer when encountering a used character
    - remember to use the max when moving the pointer
    - store the position after the character (i + 1)
    - add 1 to size
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        l = 0
        longest = 0
        for i in range(len(s)):
            c = s[i]
            if c in char_dict:
                l = max(char_dict[c], l)
            char_dict[c] = i + 1 
            longest = max(longest, i-l + 1)
        
        return longest