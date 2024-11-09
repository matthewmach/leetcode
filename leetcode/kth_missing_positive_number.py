"""
Solution:
- Brute force: O(n)
- binary search: O(logn)
    - Big Observation: the index of the element minus the element itself is the number of missing elements at that point
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot -1
        
        return left + k
