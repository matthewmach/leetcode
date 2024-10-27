"""
Input:
    - 0 indexed array of ints, w
        - represents the weight of index i 
Output:
    - every time pickIndex() is called, returns random value i based on weights

Solution:
    - naive, use random() mod sum of weights 
        - compute sum of consecutive elements (prefix sum) from w and compare until you find the value in between 2 indexes
            - can be sped up by binary search
        - Space complexity = O(n)
        - Time complexity = O(n) worst case if search, O(log n) if binary 
    - another idea, add the index w[i] times to a list and use random.choice()
        - space complexity is horrible sum of w[i]
"""

import random
class Solution:
    def __init__ (self, w : list[int]):
        self.sums = []
        s = 0
        for i in w:
            s += i
            self.sums.append(s)
        self.max = s

    def pickIndexLinear(self) -> int:
        rnd = random.randint(0, self.max)
        for i, s in enumerate(self.sums):
            if rnd <= s:
                return i 

    ### Binary
    def pickIndex(self) -> int:
        rnd = self.max * random.random()
        start, end = 0, len(self.sums)
        while start < end:
            m = start + (end - start) // 2

            if self.sums[m] == rnd:
                return m
            if self.sums[m] < rnd:
                start = m + 1
            elif self.sums[m] > rnd:
                end = m
        ## ends with start > end, return the higher value
        return start