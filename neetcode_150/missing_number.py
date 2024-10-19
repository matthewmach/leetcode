class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s += i
        n = len(nums)
        return int(n*(n+1)/2) - s