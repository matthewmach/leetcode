"""
- just sort then iterate through
"""

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        arr.sort()
        for a in arr:
            dic[a] += 1
  
        for key in dic:

            print (dic)
            if dic[key] > 0:
                if key % 2 == 0 and key < 1 and key//2 in dic:
                    pairs = min(dic[key], dic[key//2])
                    dic[key] -= pairs
                    if key != 0:
                        dic[key//2] -= pairs
                elif key*2 in dic:
                    pairs = min(dic[key], dic[key*2])
                    dic[key] -= pairs
                    dic[key*2] -= pairs
                else:
                    return False
        for key in dic:
            if dic[key] != 0:
                return False
        return True