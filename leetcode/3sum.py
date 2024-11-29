"""
- n^2 solution is get the sum of every pair and then search in the hash table for a sum
- two pointer O(n^2) with sort
    - sort the list, for loop i going through each one
    - take two pointers after i and at the end of the list
    - n * n operations + nlogn
    - if i (the smallest number) > 0, then we obviously can't form 0
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
        
        return out


    def hashmap_bad(self, nums: List[int]) -> List[List[int]]:
        dupes = set()
        pair_sums = defaultdict(list)
        triplets = set()
        for i, vali in enumerate(nums):
            if vali not in dupes:
                dupes.add(vali)
                for j, valj in enumerate(nums[i+1:]):
                    complement = -(vali + valj)
                    if complement in pair_sums and pair_sums[complement] == i:
                        triplets.add(tuple(sorted([vali, valj, complement])))
                    pair_sums[valj] = i
        return [list(x) for x in triplets]
