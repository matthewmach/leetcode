class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        out = nums[0]
        for i in nums:
            cur_sum += i
            out = max(out, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return out