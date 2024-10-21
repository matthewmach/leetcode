class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        i = 0
        while True:
            if i > len(word1) - 1:
                out = out + word2[i:]
                break
            if i > len(word2) - 1:
                out = out + word1[i:]
                break
            
            out = out + word1[i] + word2[i]
            i += 1
        return out