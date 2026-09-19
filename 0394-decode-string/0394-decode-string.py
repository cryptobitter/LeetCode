class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_num = 0
        current_str = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ""
            elif ch == ']':
                prev_num = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + prev_num * current_str
            else:
                current_str += ch

        return current_str