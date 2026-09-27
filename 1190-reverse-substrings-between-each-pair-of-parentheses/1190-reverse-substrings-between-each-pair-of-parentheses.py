class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for char in s:
            if char == '(':
                stack.append([])
            elif char == ')':
                top = stack.pop()
                top.reverse()
                stack[-1].extend(top)
            else:
                stack[-1].append(char)
        return ''.join(stack[0])