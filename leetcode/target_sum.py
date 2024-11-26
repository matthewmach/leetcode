from functools import cache

def findTargetSumWays(self, nums: list[int], target: int) -> int:
    @cache
    def helper(ind: int, s: int):
        if ind == len(nums):
            if s == target:
                return 1
            else:
                return 0
        return helper(ind+1, s+nums[ind]) + helper(ind+1, s-nums[ind])

    return helper(0, 0)