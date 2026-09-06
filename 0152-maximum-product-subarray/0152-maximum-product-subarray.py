class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = best = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * cur_max, num * cur_min)
            cur_max = temp_max
            
            best = max(best, cur_max)
            
        return best