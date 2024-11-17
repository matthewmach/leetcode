"""
Solution:
- initial ideas
    - can only add / multiply when current number is less than target? (might not be true because you might have to get a bigger number to subtract later)
    - numbers can be more than one digit like 12 - 3
    - output is a string
    - recursive solution
        - answer is O(4^n) (add, subtract, multi, leave number)
    - rememeber 0 cases
        - all zero case
    - problems with the first number 
    - dfs
"""



class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        out = []
        def helper(cur_str, total, prev_num, i):
            if i == len(num):
                if total == target:
                    out.append(cur_str)
            else:
                for j in range(i, len(num)):
                    if j > i and num[i] == "0": 
                        break
                    
                    cur_num = int(num[i:j+1])
                    if i == 0:
                        helper(cur_str + str(cur_num), total + cur_num, cur_num, j+1)
                    else:
                        helper(cur_str + "+" + str(cur_num), total + cur_num, int(cur_num), j+1)
                        helper(cur_str + "-" + str(cur_num), total - cur_num, -int(cur_num), j+1)
                        helper(cur_str + "*" + str(cur_num), total - prev_num + prev_num * cur_num, cur_num * prev_num, j+1)

        helper("", 0, 0, 0)
        return out
