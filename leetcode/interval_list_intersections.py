"""
Input: two lists of intervals
Output: list of overlaping intervals

Sol:
- one pointer for each list
- check intersection
- iterate whichever point contains the further interval

- better solution
    - merge the intervals and always take the further interval
"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        out = []

        while first < len(firstList) and second < len(secondList):
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])
            if start <= end:
                out.append([start, end])
            
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1
        
        return out