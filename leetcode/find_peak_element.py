"""
Input: integer array
output: index of any peak

Solution:
- log n imples some sort of binary search
- idea: elements can either be in ascending or descending slope 
- goal is to find the peak of this ascending slope
- if it's descending, then go backwards
- if it's ascending, then go forwards 
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r, = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return l