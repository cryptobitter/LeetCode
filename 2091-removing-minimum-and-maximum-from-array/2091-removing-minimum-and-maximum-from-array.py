class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=0
        maxi=0
        for i in range(len(nums)):
            if nums[i] > nums[maxi]:
                maxi=i
            if nums[i] < nums[mini]:
                mini=i
        
        lo , hi = min(mini,maxi) , max(mini,maxi)
        remove_front=hi + 1
        remove_back= len(nums)-lo
        from_both_end=(len(nums)-hi)+(lo+1)
        return min(remove_front,remove_back,from_both_end)