# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic.keys():
                return True
            else:
                dic[num] = 1
        return False


    # If the set has a dupe number, the set will have diff length
    def hash_set_length(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)