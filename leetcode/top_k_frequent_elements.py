"""
Input: integer array nums and number of frequent elements
Output: top k frequent elements

Solution:
- sort array
- push a pair of frequency and number to a heap
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        top_elements = []
        heapq.heapify(top_elements)

        cur_num = nums[0]
        count = 0
        print(nums[-1])
        for i in nums:
            if i == cur_num:
                count += 1
            else:
                if len(top_elements) < k:
                    heapq.heappush(top_elements, (count, cur_num))
                elif count > top_elements[0][0]:
                    heapq.heappushpop(top_elements, (count, cur_num))
                cur_num = i
                count = 1

        if len(top_elements) < k:
            heapq.heappush(top_elements, (count, cur_num))
        elif count > top_elements[0][0]:
            heapq.heappushpop(top_elements, (count, cur_num))

        out = []
        for ele in top_elements:
            out.append(ele[1])

        return out