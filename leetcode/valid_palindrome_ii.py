# Notes: need to choose which letter to delete as it could be possible to delete 2 diff
#        need recursion for both choices 
class Solution:
    def recursion(self, s: str) -> bool:
        def helper(start, end, replace) -> bool:
            if s[start] != s[end]:
                if not replace:
                    return helper(start+1, end, True) or helper(start, end-1, True)
                else:
                    return False
            if start >= end:
                return True
            return helper(start+1, end-1, replace)

        return helper(0, len(s)-1, False)
    
    # Normally for palendromes just do s == s[::-1], but for this you have to actively search for wrong char
    # Once you find the wrong char you can just perform the check without it
    def two_pointer(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start <= end:
            if s[start] != s[end]:
                # Create strings without each char and just directly check
                s1 = s[:start] + s[start+1:]
                s2 = s[:end] + s[end+1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            start += 1
            end -= 1
        return True