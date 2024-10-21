# Idea: Calculate the transformation of every point and find the max of the same transformation
# Faster Idea: use bit shifting to form binary numbers equivalent to each row
#              compare rows by shifting bits left and right or comparing up or down
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_p, img2_p, trans = [], [], defaultdict(int)

        for x in range(len(img1)):
            for y in range(len(img1[0])):
                if img1[x][y]:
                    img1_p.append([x,y])
                if img2[x][y]:
                    img2_p.append([x,y])
        out = 0
        for p1 in img1_p:
            for p2 in img2_p:
                trans[(p2[0]-p1[0], p2[1]-p1[1])] += 1
                out = max(out, trans[(p2[0]-p1[0], p2[1]-p1[1])])
        return out