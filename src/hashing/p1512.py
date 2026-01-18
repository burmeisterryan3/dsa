"""https://leetcode.com/problems/number-of-good-pairs/description/"""

from collections import defaultdict
from math import comb

class Solution:
    def num_identical_pairs(self, nums: list[int]) -> int:
        tracker = defaultdict(int)
        ans = 0
        for num in nums:
            tracker[num] += 1
        
        for v in tracker.values():
            if v > 1:
                ans += comb(v, 2)
        
        return ans