class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid = 0
        while mid < len(nums) and nums[mid] < 0:
            mid += 1

        out = []
        l, r = mid-1, mid
        while True:
            if r == len(nums):
                while l >= 0:
                    out.append(pow(nums[l], 2))
                    l -= 1
                return out
            if l < 0:
                while r < len(nums):
                    out.append(pow(nums[r], 2))
                    r += 1
                return out
            
            if nums[r] > abs(nums[l]):
                out.append(pow(nums[l], 2))
                l -= 1
            else:
                out.append(pow(nums[r], 2))
                r += 1
        
        return out