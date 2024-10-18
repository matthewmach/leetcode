from collections import defaultdict

class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(list)
        start= 0
        max_l = 0
        for i, c in enumerate(s):
            if c in dic:            
                max_l = max(max_l, i-start)
                start = max(start, dic[c][-1] + 1)
            dic[c].append(i)

        if len(s) - start > max_l:
            max_l = len(s) - start

        return max_l

    # Time Complexity: O(n)
    # Space Complexity: worst case O(n)
    def sliding_window(self, s: str) -> int:
        charSet = set()
        l = 0
        out = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove[s[l]]
                l += 1
            charSet.add[s[r]]
            out = max(out, r-l+1)
        return out