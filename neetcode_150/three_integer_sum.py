class Solution:
    # Time Complexity: O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        # Space Complexity: Worst Case O(n), Best Case O(1)
        nums.sort()

        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums [x-1]:
                continue
            y = x + 1
            z = len(nums)-1
            while y < z:
                print(f"{x} {y} {z}")
                three_sum = nums[x] + nums[y] + nums[z]
                if three_sum == 0:
                    out.append([nums[x], nums[y], nums[z]])
                    y += 1
                    z -= 1
                    while nums[y] == nums[y-1] and y < z:
                        y += 1
                elif three_sum > 0:
                    z -= 1
                else:
                    y += 1
        return out
