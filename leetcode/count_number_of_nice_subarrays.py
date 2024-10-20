# Idea: subarrays of k odd elements, have possible prefixes and suffixes
#       traverse from left to right
#       start incrementing suffix as soon as you find k odd elements
#       if you have k+1 odd, remove elements until you remove an odd, this is your prefix
#       prefix * suffix subarrays from that group of odd numbers
#       two-pointer sol

# Another idea: parse array for odd numbers
#               prefix = start or last odd -> first odd
#               suffix = last odd -> next odd or end
#               uses more memory
#               set sol
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        start = 0
        out = 0
        suffix = 1
        for n in nums:
            if n % 2 == 1:
                odd += 1
            elif odd == k:
                suffix += 1
            if odd > k:
                prefix = 1
                while nums[start] % 2 != 1:
                    start += 1
                    prefix += 1
                start += 1
                out += prefix * suffix
                prefix = 1
                suffix = 1
                odd -= 1

        if odd == k:
            prefix = 1
            while nums[start] % 2 != 1:
                start += 1
                prefix += 1
            print (suffix, prefix)
            out += prefix * suffix
        return out