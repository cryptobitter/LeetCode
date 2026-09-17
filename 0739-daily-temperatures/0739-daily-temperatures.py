class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack =[]
        result =[0]*len(temperatures)
        for i , temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j=stack.pop()
                result[j] =i-j
            stack.append(i)
        return result