"""
keep current sum, as soon as it's negative, start at 0 again
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            cur_sum = max(cur_sum, 0)
        
        return max_sum