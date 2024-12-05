"""
O(n) recursion with visited?
- greedy is you recurse from the back and you keep a counter of what the closest node you can reach
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= can_reach:
                can_reach = i
        return can_reach == 0
        