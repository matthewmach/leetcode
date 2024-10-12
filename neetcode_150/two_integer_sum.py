class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                print (f"{i} {j}")
                s = nums[i] + nums[j]
                if s == target:
                    return [i, j]

    # Time Complexity: O(n)
    # Space Complexity: O(n) worst case
    def optimal(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[diff] = i