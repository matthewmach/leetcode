"""
Initial thought naive sol:
- keep dict of colors, set for each, delete add in O(1)
- n adds, at most n deletions 
- uses a ton of memory but fast
"""
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(set)
        balls = defaultdict(int)
        out = []
        distinct = 0
        for x, color in queries:
            #print (colors, balls)
            if not colors[color]:
                distinct += 1
            if x in balls:
                if balls[x] == color:
                    out.append(distinct)
                    continue
                colors[balls[x]].remove(x)
                if not colors[balls[x]]:
                    distinct -= 1
            colors[color].add(x)
            balls[x] = color    
            out.append(distinct)
        return out
