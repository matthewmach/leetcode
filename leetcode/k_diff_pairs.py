class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = defaultdict(list)
        for i in range(len(nums)):
            s[nums[i]].append(i)

        out = 0
        for key in s:
            if k == 0:
                if len(s[key]) > 1:
                    out += 1 
            elif key + k in s:
                out += 1

        return out