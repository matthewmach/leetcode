"""
Solution:
- stack problem, start popping with negative number
- lots of side cases
    - negative numbers
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        for a in asteroids:
            if a > 0 or not out or (out[-1] < 0 and a < 0):
                out.append(a)
            else:
                cur = out.pop()
                while True:
                    if cur > 0:
                        if abs(a) > cur:
                            if out:
                                cur = out.pop()
                                continue
                            out.append(a)
                        if abs(a) < cur:
                            out.append(cur)
                    else:
                        out.append(cur)
                        out.append(a)
                    break
                
        return out