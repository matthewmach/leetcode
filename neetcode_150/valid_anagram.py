# Time Complexity: O(N)
# Space Complexity: 26 letters = O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1
        for c in t:
            if c in dic.keys():
                dic[c] -= 1
            else:
                return False
        for key, value in dic.items():
            if value != 0:
                return False
        return True