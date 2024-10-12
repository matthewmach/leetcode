from operator import itemgetter
class Solution:
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        l = []
        for key,value in dic.items():
            l.append([key, value])
        l = sorted(l, key=lambda x: x[1])

        ans = []
        for i in range(1, k+1):
            ans.append(l[-i][0])
        return ans

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    '''
    Notes:
        - idea: bucket sort the frequencies of each numbers and iterate backwards until you have all the values you need
        - max frequency is n
        - so O(n) to get frequencies, O(n) to bucket sort, O(n) to get desired elements
    '''
    def optimal(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        out = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]
                out.append(num)
                if len(out) == k:
                    return out