class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=prev2=0
        for num in nums:
            cur =max(prev,prev2+num)
            prev2=prev
            prev=cur
        return prev