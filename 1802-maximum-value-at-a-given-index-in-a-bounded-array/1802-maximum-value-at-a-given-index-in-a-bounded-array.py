class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(v, cnt):
            if v >= cnt:
                return (v + v - cnt + 1) * cnt // 2
            else:
                return (v + 1) * v // 2 + (cnt - v)
        
        left, right = 1, maxSum
        
        while left < right:
            mid = (left + right + 1) // 2
            total = getSum(mid, index + 1) + getSum(mid, n - index) - mid
            if total <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left