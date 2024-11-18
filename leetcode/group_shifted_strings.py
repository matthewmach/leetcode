"""
Solution:
- idea, subtract every character in the string by the first character mod 26
    - shifts everything to first character a
    - everything in the same shifting sequence 
    - append string to dict
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shift_dic = defaultdict(list)
        for string in strings:
            sequence = []
            for c in string:
                sequence.append((ord(c) - ord(string[0])) % 26)
            shift_dic[tuple(sequence)].append(string)
        out = []
        for key in shift_dic:
            out.append(shift_dic[key])
        return out