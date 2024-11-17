"""
Just set the first string to the prefix and decrease it for each comparision
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        length = len(prefix)

        for s in strs[1::]:
            while prefix != s[0:length]:
                length -= 1
                if length == 0:
                    return ""
                prefix = prefix[0:length]
        
        return prefix