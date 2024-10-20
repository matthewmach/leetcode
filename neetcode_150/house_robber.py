class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for i in range(0, len(nums)):
            tmp = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = tmp
        return prev1