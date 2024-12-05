class Solution:

    def __init__(self, nums: List[int]):
        self.num_dict = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_dict[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.num_dict[target])        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)