class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        out = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_height:
               out.append(i)
               max_height = heights[i]

        return out[::-1] 
        