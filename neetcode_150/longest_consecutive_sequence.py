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
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res