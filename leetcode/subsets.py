"""
Solution
- O(n * 2^n)
- either include the element or not in the set, keep adding both the output and the set
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = set()

        def helper(i, current):
            out.add(tuple(current))
            if i == len(nums):
                return
            helper(i+1, current + [nums[i]])
            helper(i+1, current)

        helper(0, [])
        return [list(t) for t in list(out)]