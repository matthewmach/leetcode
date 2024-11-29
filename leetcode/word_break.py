"""
Every part of the string has to be part of the dict
- maybe find largest string
- iterate through the string until you find a word
    - reset the word
        - what if a word is contained in a word like door and doorknob
        - get max length word and stop that instance when you can't find a word
    - O(n) worst case O(n^2)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        wordDict = set(wordDict)
        @cache
        def helper(i, word):
            if i == len(s):
                if word:
                    return False
                return True
            word = word + s[i]
            if len(word) <= maxLen:
                found = False
                if word in wordDict:
                    found = helper(i+1, "")
                return found or helper(i+1, word)
            else:
                return False
        
        return helper(0, "")