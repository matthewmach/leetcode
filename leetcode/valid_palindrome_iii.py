"""
Solution:
- memotization is n^2 for space and time complex
"""

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
            @cache
            def isPal(i, j, count):
                if count < 0:
                    return False
                if i >= j:
                    return True
                
                if s[i] == s[j]:
                    return isPal(i+1, j-1, count)
                else:
                    return isPal(i+1, j, count -1) or isPal(i, j-1, count-1)
            
            return isPal(0, len(s) - 1, k)
    
    def isValidPalindrome(self, s: str, k: int) -> bool:
            palin_memo = {}
            def isPal(i, j, count):
                if count < 0:
                    return False
                if i >= j:
                    return True
                tup = (i, j, count)
                
                if tup not in palin_memo:
                    if s[i] == s[j]:
                        palin_memo[tup] = isPal(i+1, j-1, count)
                    else:
                        palin_memo[tup] = isPal(i+1, j, count -1) or isPal(i, j-1, count-1)
                return palin_memo[tup]
                    
            
            return isPal(0, len(s) - 1, k)