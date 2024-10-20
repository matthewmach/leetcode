class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        s = {}
        for n in nums:
            s[n] = 0
        
        longest = 0
        for key in s:
            if s[key] == 1:
                pass
            else:
                while key-1 in s:
                    key -= 1
                streak = 1
                while key+1 in s:
                    key += 1
                    streak += 1
                    s[key] = 1
                if streak > longest:
                    longest = streak
        return longest
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def optimal(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        out = 0
        for n in nums:
            if dic[n] == 0:
                dic[n] = 1 + dic[n-1] + dic[n+1]
                # Only have to update ends of the sequence (this will update nums that may not exist)
                dic[n-dic[n-1]], dic[n+dic[n+1]] = dic[n], dic[n]
                out = max(out, dic[n])
        return out