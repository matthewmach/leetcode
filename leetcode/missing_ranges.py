"""
Solution:
- since nums is ordered, iterate through nums adding range of the differences between the numbers
- remember negative numbers
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        out = []
        last_num = lower-1
        nums.append(upper+1)
        for n in nums:
            if abs(n - last_num) > 1:
                out.append([last_num+1, n-1])
            last_num = n
        return out