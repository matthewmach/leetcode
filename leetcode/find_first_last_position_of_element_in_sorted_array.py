"""
- quickselect target value?
- what does starting and ending position mean?
- just first and last if it exists?

- binary search into iterating from element found until last and first occurance found?
- beware of edge cases!!! like empty arrays
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) -1
        if start == end and nums[start] == target:
            return [start, start]
        mid = 0

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if not nums or nums[mid] != target:
            return [-1, -1]
        

        out = [mid, mid]
        while out[0] > 0 and nums[out[0]-1] == target:
            out[0] -= 1
        while out[1] < len(nums)-1 and nums[out[1] +1] == target:
            out[1] += 1
        return out