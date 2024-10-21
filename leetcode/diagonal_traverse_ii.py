# Observation: all diagonals share the same x + y sum
class Solution:
    def hashTable(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for y in range(len(nums)):
            for x in range(len(nums[y])):
                d[x+y].append(nums[y][x])
        out = []
        for key in d:
            out = out + d[key][::-1]
        return out

# better observation: each diagonal value is a reflection of each other
# use a dual ended queue or just query [-1] and keep appending reflections
# each time you go through an element, the next one to query will be to the right (unless col == 0 then bottom)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0, 0)])
        ans = []
        
        while queue:
            row, col = queue.popleft()
            print (row, col, nums[row][col])
            ans.append(nums[row][col])
            
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))
                
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
        
        return ans
