# n^2 + n^2 + n
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d12 = defaultdict(list)
        for n1 in nums1:
            for n2 in nums2:
                d12[n1+n2].append([n1, n2])
        
        d34 = defaultdict(list)
        for n3 in nums3:
            for n4 in nums4:
                d34[n3+n4].append([n3, n4])
        
        out = 0
        for key in d12:
            if -key in d34:
                out += len(d12[key]) * len(d34[-key])
        return out