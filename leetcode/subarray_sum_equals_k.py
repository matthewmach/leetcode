"""
Solution:
- sliding window of subarrays
- hashmap of all sums to that point
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = 0
        sums = defaultdict(int)
        sums[0] = 1
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if (cur_sum - k) in sums:
                out += sums[cur_sum - k]
            sums[cur_sum] += 1

        return out