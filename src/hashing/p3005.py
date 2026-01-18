"""https://leetcode.com/problems/count-elements-with-maximum-frequency/description/"""

from collections import defaultdict, Counter

class Solution:
    def max_frequency_elements(self, nums: list[int]) -> int:
        tracker = defaultdict(int)
        mx = 0
        for num in nums:
            tracker[num] += 1
            mx = max(tracker[num], mx)
        
        print(tracker)
        ans = 0
        for v in tracker.values():
            if v == mx:
                ans += v
        
        return ans

    def max_frequency_elements_counter(self, nums: list[int]) -> int:
        tracker = Counter(nums)
        mx = max(tracker.values())
        
        ans = 0
        for v in tracker.values():
            if v == mx:
                ans += v

        return ans