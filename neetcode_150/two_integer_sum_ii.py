class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        bot = 0
        top = len(numbers)-1

        while True:
            s = numbers[bot] + numbers[top]
            if s == target:
                return [bot+1, top+1]
            elif s > target:
                top -= 1
            else:
                bot += 1