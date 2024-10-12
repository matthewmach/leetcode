class Solution:
    # Time Complexity: O(nmlogm)
    # Space Complexity: O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in m:
                m[sort].append(s)
            else:
                m[sort] = [s]
        out = []
        for key, value in m.items():
            out.append(value)
        return out

    # Time Complexity: O(mn)
    # Space Complexity: O(m)
    '''
    Notes:
        - Tuples are unmutable so are usable as dict keys
        - defaultdict(list).values will return as a 2d list
    '''
    def optimal(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values