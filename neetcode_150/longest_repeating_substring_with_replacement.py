class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(26)
    """ 
    idea: slide window keeping length - max_count <= k and a dict of frequencies 
    max_count only gets incremented if we have a new high
    answer is min of max_count + k and len(s)
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxc = 0
        l = 0
        for i in range(len(s)):
            count[s[i]] += 1
            
            maxc = max(maxc, count[s[i]])
            if (i - l + 1) - maxc > k:
                count[s[l]] -= 1
                l += 1

        return min(len(s), maxc + k)   