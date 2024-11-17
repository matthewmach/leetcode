"""
Solution
- stack, assumes that a function cannot end while in the background
- each time something end, pop the top, add the difference in current time and end time
- subtract the difference in time from the next element as it cannot run for that time
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        call_stack = []
        exec_time = [0] * n

        for log in logs:
            call = log.split(":")
            if call[1] == "start":
                call_stack.append((int(call[0]), int(call[2])))
            else:
                top = call_stack.pop()
                exec_time[top[0]] += int(call[2]) - top[1] + 1
                if call_stack:
                    exec_time[call_stack[-1][0]] -= int(call[2]) - top[1] + 1
        
        return exec_time