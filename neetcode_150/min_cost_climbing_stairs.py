class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(ind, cost) -> int:
            if ind > len(cost) - 1:
                return 0
            one = helper(ind+1, cost) + cost[ind]
            two = helper(ind+2, cost) + cost[ind]
            return min(one, two)

        zero = helper(0, cost)
        one = helper(1, cost)
        return min(zero, one)