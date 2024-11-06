"""
Solution:
- two pointers
- keep counter of until k zeroes
- increment end pointer every time you get to k+1 zeroes
- increment start pointer until k zeroes
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end = 0, 0
        zeroes = 0
        m = 0
        while end < len(nums):
            print (start, end)
            if nums[end] == 0:
                zeroes += 1
            
            m = max(m, end-start)
            end += 1

            if zeroes > k:
                start += 1
                while start-1 < len(nums) and nums[start-1] != 0:
                    start += 1
                zeroes -= 1
        
        return max(m, end-start)