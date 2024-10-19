class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            num = 0
            for d in str(n):
                num += pow(int(d), 2)
            if num in s:
                return False
            else:
                s.add(num)
            n = num
        return True

    # Intended sol is 2 pointer, slow and fast