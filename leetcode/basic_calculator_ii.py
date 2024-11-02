"""
Idea:
    - pass through string and evaluate * and / left to right first, editing the string in place
    - pass through second time and evaluate + and -
    - Time Complexity: O(n) + O(n) (well technically if you edit in place the numbers get bigger)

    - split string by * or / until you can't (problem is you have to split twice and check which one has the smaller left side)
        - iterate once through the string O(n) to get all * and /, and + and - then iterate through those arrays
    - time complexity O(n) + O(n/2) worst case (all one digit numbers)
    - Space complexity: O(n/2)

    - evaluate digit by digit, keeping stack of numbers to add, pop and add to stack after multiplication or division

    - instead of stack just track last number and result
"""

class Solution:
    def calculate(self, s: str) -> int:
        out = 0
        cur_num = 0
        prev_num = 0
        prev_op = "+"

        for c in s + "+":
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == " ":
                continue
            elif c in "-+":
                match prev_op:
                    case "+":
                        out += cur_num
                    case "-":
                        out -= cur_num
                    case "*":
                        out += prev_num * cur_num
                    case "/":
                        print (f"{prev_num} {cur_num}")
                        out += int(prev_num / cur_num)
                cur_num, prev_num = 0, 0
                prev_op = c
            elif c in "*/":
                match prev_op:
                    case "+":
                        prev_num = cur_num
                    case "-":
                        prev_num = -cur_num
                    case "*":
                        prev_num = prev_num * cur_num
                    case "/":
                        prev_num = int(prev_num / cur_num)
                cur_num = 0
                prev_op = c
        return int(out)