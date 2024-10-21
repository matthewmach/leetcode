class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        out = 0
        dic = defaultdict(int)
        for w in words:
            dic[w] += 1

        mid = 0
        for key in dic:
            if key == key[::-1]:
                if dic[key] % 2 == 1:
                    mid = 1 
                out += dic[key] // 2
            elif key[::-1] in dic:
                out += min (dic[key], dic[key[::-1]])
                dic[key] = 0

        return (out*2 + mid)*2