"""https://leetcode.com/problems/sum-of-unique-elements/description/"""

from collections import defaultdict, Counter

class Solution:
    def sum_of_unique(self, nums: list[int]) -> int:
        tracker = defaultdict(int)
        for num in nums:
            tracker[num] += 1

        ans = 0
        for k, v in tracker.items():
            if v == 1:
                ans += k
        
        return ans
    
    def sum_of_unique_pythonic(self, nums: list[int]) -> int:
        return sum(dict(filter(lambda x: x[1] == 1, Counter(nums).items())))
    
    def sum_of_unique_counter(self, nums: list[int]) -> int:
        nums = Counter(nums)
        total = 0
        for k, v in nums.items():
            if v == 1:
                total += k
        return total