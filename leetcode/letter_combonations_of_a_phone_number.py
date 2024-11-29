"""
recursion
- O(n * 4^n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        out = []
        mapping = {
            "2":["a", "b", "c"],
            '3':["d", "e", "f"],
            '4':["g", "h", "i"],
            '5':["j", "k", "l"],
            '6':["m", "n", "o"],
            '7':["p", "q", "r", "s"],
            '8':["t", "u", "v"],
            '9':["w", "x", "y", "z"]
        }
        def helper(i, combo):
            if i == len(digits):
                if len(combo) == len(digits):
                    out.append(combo)
                return

            for letter in mapping[digits[i]]:
                helper(i+1, combo + letter)
            helper(i+1, combo)

        helper(0, "")
        return out