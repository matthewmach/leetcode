class Solution:
    def calculate_no(self, s: str) -> int:
        out = 0
        cur_num = 0
        prev_num = 0
        prev_op = "+"
        prev_c = ""
        negative = False

        for c in s + "+":
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == " ":
                continue
            elif c in {"+", "-"}:
                if c == "-" and prev_c in {"+", "-", "/", "*"}:
                    negative = not negative
                else:
                    if negative:
                        cur_num = -cur_num
                    match prev_op:
                        case "+":
                            out += cur_num
                        case "-":
                            out -= cur_num
                        case "*":
                            out += prev_num * cur_num
                        case "/":
                            out += prev_num // cur_num
                    cur_num, prev_num = 0, 0
                    negative = False
                    prev_op = c
            elif c in {"*", "/"}:
                match prev_op:
                    case "+":
                        prev_num = cur_num
                    case "-":
                        prev_num = -cur_num
                    case "*":
                        prev_num = prev_num * cur_num
                    case "/":
                        prev_num = prev_num // cur_num
                cur_num = 0
                prev_op = c
            prev_c = c
        
        return out

    def calculate(self, s: str) -> int:
        parenthesis_stack = []
        cur_str = ""

        for c in s:
            if c == " ":
                continue
            elif c == "(":
                parenthesis_stack.append(cur_str)
                cur_str = ""
            elif c == ")":
                val = self.calculate_no(cur_str)
                cur_str = parenthesis_stack.pop()
                cur_str = cur_str + str(val)
            else:
                cur_str = cur_str + c
        
        return self.calculate_no(cur_str)