class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    '''
    Notes
        - need delimiter, can put length but you need to know when the length ends, so length + special char to encode
    '''
    def encode(self, strs: list[str]) -> str:
        out = ""
        for str in strs:
            out = out + f"{len(str)}" + "#" + str
        return out

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def decode(self, s: str) -> list[str]:
        out = []
        ind = 0
        while ind < len(s):
            c = s[ind]
            num = ""
            while c != '#':
                num = num + c
                ind += 1
                c = s[ind]

            l = int(num)
            ind += 1
            new = ""
            for i in range(l):
                new = new + s[ind]
                ind += 1
            out.append(new)
        return out