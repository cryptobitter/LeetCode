from typing import List
from collections import defaultdict

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        freq = defaultdict(int)

        for num in nums:
            r = num % k
            new_freq = defaultdict(int)
            new_freq[r] += 1                 
            for rem, cnt in freq.items():
                nr = (rem * num) % k
                new_freq[nr] += cnt

            for rem, cnt in new_freq.items():
                result[rem] += cnt

            freq = new_freq

        return result