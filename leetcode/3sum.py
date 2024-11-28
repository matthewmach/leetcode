"""
- n^2 solution is get the sum of every pair and then search in the hash table for a sum
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
