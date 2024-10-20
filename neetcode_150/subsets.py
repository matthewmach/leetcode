class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for s in range(len(subsets)):
                subsets.append(subsets[s] + [num])
        return subsets
    
    def dfs(self, nums: List[int]) -> List[List[int]]:
        out = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                out.append(subset.copy())
                return
            subset.append(nums[i])
            # dfs like you added the element
            dfs(i+1)
            subset.pop()
            # dfs like you didn't add the element
            dfs(i+1)
        dfs(0)
        return out