"""
Input: Permutation in array
Output: next permutation

Solution:
- lexographical order
- each thing is compared digit by digit
- 
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            i -= 1

        if i == 0:
            nums.reverse()
        else:
            nxt = len(nums) - 1
            while nums[nxt] <= nums[i-1]:
                nxt -= 1

            print(i, nxt)
            tmp = nums[i-1]
            nums[i-1] = nums[nxt]
            nums[nxt] = tmp
            nums[i::] = nums[i::][::-1]
