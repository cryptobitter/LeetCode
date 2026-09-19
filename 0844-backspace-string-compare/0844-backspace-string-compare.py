class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            if stack and i == "#":
                stack.pop()
            else:
                if i != '#':
                    stack.append(i)
                else:
                    continue
        stack2=[]
        for j in t:
            if stack2 and j == "#":
                stack2.pop()
            else:
                if j != '#':
                    stack2.append(j)
                else:
                    continue
        return stack == stack2
      