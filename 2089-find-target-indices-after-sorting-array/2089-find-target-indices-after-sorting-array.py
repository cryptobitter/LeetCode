class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        a=sorted(nums)
        b=[]
        for i in range(len(nums)):
            if a[i] == target:
                b.append(i)
        return b
