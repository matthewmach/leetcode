class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occur = []
        for i in range(len(nums)):
            if nums[i] == x:
                occur.append(i)
        
        out = []
        for q in queries:
            out.append(-1 if q > len(occur) else occur[q-1])
        return out