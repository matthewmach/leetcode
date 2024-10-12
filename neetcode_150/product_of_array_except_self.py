class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        prod = 1
        for n in nums:
            if n == 0:
                zeroes += 1
            else:
                prod *= n
        out = []
        for n in nums:
            if zeroes > 1:
                out.append(0)
            elif zeroes == 1:
                if n == 0:
                    out.append(prod)
                else:
                    out.append(0)
            else:
                out.append(int(prod/n))
        return out

    # Time Complexity: n + n = O(n)
    # Space Complexity: O(1)
    def no_div(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            out[i] *= postfix
            postfix *= nums[i]
        return out



