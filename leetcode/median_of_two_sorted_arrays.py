"""
idea
- binary search one list only
- for the number to be a median of both the lists combined, it has to have x amount of elements in nums1, and half-x elements in nums2
    - that means we only have to binary search one array and check to see if the elements at x in nums1 are contained within the elements of half-x in num2
    - in other words, nums1[mid] <= nums2[half-mid+1] and nums2[half-mid] <= nums1[mid+1]
- binary search the smaller array as it's faster
- O(log(min(m,n)))
"""
class Solution:
    def correct(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l+r) // 2
            j = half - i - 2

            Aleft = A[i] if i >=0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_len = len(nums1) + len(nums2)
        half = merged_len // 2

        if len (nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        while True:
            mid1 = (l+r) // 2
            mid2 = half - (mid1 + 1) - 1

            nums1Mid = nums1[mid1] if mid1 >= 0 else float("-infinity")
            nums1Right = nums1[mid1+1] if (mid1+1) < len(nums1) else float("infinity")

            nums2Mid = nums2[mid2] if mid2 >= 0 else float("-infinity")
            nums2Right = nums2[mid2+1] if (mid2 + 1) < len(nums2) else float("infinity")

            if nums1Mid <= nums2Right and nums2Mid <= nums1Right:
                if merged_len % 2 == 1:
                    return min(nums1Right, nums2Right)
                return (min(nums1Right, nums2Right) + max(nums1Mid, nums2Mid)) / 2
            elif nums1Mid > nums2Right:
                r = mid1 - 1
            else:
                l = mid1 + 1