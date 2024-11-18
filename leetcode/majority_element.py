class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_dict = defaultdict(int)
        majority = len(nums) // 2
        for num in nums:
            ele_dict[num] += 1
            if ele_dict[num] > majority:
                return num