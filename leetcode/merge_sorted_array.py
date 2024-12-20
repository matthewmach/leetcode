class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        # Key observation: if you iterate from top down, you don't need a temp element
        """
        i = m - 1
        j = n - 1
        while i+j+1 > -1:
            if j < 0 or (i > -1 and nums1[i] > nums2[j]):
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1