"""
Idea:
- store length and non zero values in dictionary or pairs of index + value
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.len = len(nums)
        self.values = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.values[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        out = 0
        for i in range(self.len):
            if i in self.values and i in vec.values:
                out += self.values[i] * vec.values[i]
        return out

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)