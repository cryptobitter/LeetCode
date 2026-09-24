class Solution:
    def digitSum(self, a: int) -> int:
        su = 0
        while a:
            su += a % 10
            a = a // 10
        return su

        
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.digitSum(nums[i]) == i:
                return i 
        return -1