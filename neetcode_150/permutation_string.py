class Solution:
    # Time Complexity: O(n*26)
    # Space Complexity: Worst case - O(26 * 2)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = defaultdict(int)
        for c in s1:
            s1_dic[c] += 1
        s2_dic = defaultdict(int)
        length = 0
        l = 0
        for i in range(len(s2)):
            s2_dic[s2[i]] += 1
            length += 1
            if length > len(s1):
                s2_dic[s2[l]] -= 1
                l += 1
                length -= 1

            if length == len(s1):
                print (s2_dic)
                same = True
                for k in s1_dic:
                    same = same and s2_dic[k] == s1_dic[k]
                if same:
                    return True

        return False
    
    # Time Complexity = O(n)
    # Space Complexity: O(26 *2)
    """
    Less comparisions both O(n)
    idea: 
    - have 2 arrays containing the number of each char
    - calculate substring array for s2 and equivalent length substring of s2
    - you want everything to match so maintain a number of matches in current substring
    - (must calculate all zero matches)
    - as you increment through, check if all num of chars match (26)
    """
    def check_sol(self, s1: str, s2:str ) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for c in s1:
            s1_count[ord(c) - ord("a")] += 1
            s2_count[ord(c) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]: matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            ind = ord(s2[r]) - ord("a")
            s2_count[ind] += 1
            if s1_count[ind] == s2_count[ind]:
                matches += 1
            elif s1_count[ind] + 1 == s2_count[ind]:
                matches -= 1

            ind = ord(s2[l]) - ord("a")
            s2_count[ind] -= 1
            if s1_count[ind] == s2_count[ind]:
                matches += 1
            elif s1_count[ind] - 1 == s2_count[ind]:
                matches -= 1
            l += 1

        return False
    
    def solution(self, s1: str, s2:str ) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26