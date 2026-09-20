class Solution:
    def reverseDegree(self, s: str) -> int:
        product=0
        for i in range(len(s)):
            val=ord(s[i])-96
            rev_val=27-val
            product=product+((i+1)*rev_val)
        return product