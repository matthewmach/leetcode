# Idea: a number xor'd with itself is 0, so by xor ing every number, you're left with the lone number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res