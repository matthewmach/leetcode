"""
- number = any characters of that amount
- no 2 numbers beside each other = number means exact amount (55 is never 5 5, always 55)
    - no leading zeros on number too
    - no zero
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_i, abbr_i = 0, 0
        while word_i < len(word) and abbr_i < len(abbr):
            if word[word_i] == abbr[abbr_i]:
                word_i += 1
                abbr_i += 1
            elif abbr[abbr_i].isnumeric():
                if abbr[abbr_i] == "0":
                    return False
                num = 0
                while abbr_i < len(abbr) and abbr[abbr_i].isnumeric():
                    num = num * 10 + int(abbr[abbr_i])
                    abbr_i += 1
                word_i += num
            else:
                return False

        return word_i == len(word) and abbr_i == len(abbr)
