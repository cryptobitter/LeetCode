class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev=prev2=0
        for i in range(len(nums)-1):
            cur=max(prev2+nums[i],prev)
            prev2=prev
            prev=cur
        a=prev
        prev=prev2=0
        for i in range(1,len(nums)):
            cur=max(prev2+nums[i],prev)
            prev2=prev
            prev=cur
        b=prev
        return max(a,b)