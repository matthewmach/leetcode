class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        index = 0
        if s == "":
            return True
            
        while index < len(s) // 2 + 1:
            if s[index] != s[-index-1]:
                return False
            index += 1
        return True