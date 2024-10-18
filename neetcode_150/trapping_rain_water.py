class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Notes: you only add when you know the other side as enough height to add
    def trap(self, height: List[int]) -> int:
        out = 0
        l, r = 0, len(height) -1
        maxL, maxR = height[l], height[r]
        while l != r:
            if maxL > maxR:
                r -= 1
                if maxR > height[r]:
                    out += maxR - height[r]
                else:
                    maxR = height[r]
            else:
                l += 1
                if maxL > height[l]:
                    out += maxL - height[l]
                else:
                    maxL = height[l]
        return out
            