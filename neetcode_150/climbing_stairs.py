class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == -1:
            return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2)