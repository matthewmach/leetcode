class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        high = 0
        for p in prices:
            if p < cur_min:
                cur_min = p
            if high < p - cur_min:
                high = p - cur_min
        if high < 0:
            return 0
        else:
            return high