class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=cur=nums[0]
        for i in range(1,len(nums)):
            cur=max(nums[i] , cur+nums[i])
            best= max(best , cur)
        return best
        