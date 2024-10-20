class Solution:
    # Time Complexity: O(n)
    def naive(self, x: float, n: int) -> float:
        if x == 0:
            return 0 
        neg = False
        if n < 0:
            neg = True
            n = abs(n)
        
        out = 1.0
        for i in range(n):
            out *= x

        if neg:
            return 1/out
        else:
            return out 

    # Time Complexity: O(log n)
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0 
        
        def helper(x, n):
            if n == 0:
                return 1
            res = helper(x, n //2)
            res = res * res if n % 2 == 0 else res * res * x 
            return res
            
        out = helper(x, abs(n))
        return out if n >= 0 else 1/out