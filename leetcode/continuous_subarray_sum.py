"""
- initial idea, brute force is n^2 as there are n^2 subarries
- check if sum is 0 % k
- any merit in mod k all numbers?
- prefix sum and set, if mod k prefix in already, then add one subarray
- what if duplicate prefix sums
    - dict over set, store count add count to number of subarries
- length of two 
    - have length count
    - delay adding sum to prefix sum set by 1 
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        sumSet = set()
        previousSum = None
        length = 0

        for num in nums:
            prefixSum = (prefixSum + num) % k
            length += 1
            if prefixSum in sumSet or (prefixSum == 0 and length > 1):
                return True
            if previousSum:
                sumSet.add(previousSum)
            previousSum = prefixSum
            
        return False