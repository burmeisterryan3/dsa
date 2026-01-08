"""https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/"""

from collections import defaultdict

class Solution:
    def max_subarray_length(self, nums: list[int], k: int) -> int:
        tracker = defaultdict(int)
        ans = left = 0

        for right, num in enumerate(nums):
            tracker[num] += 1
            while tracker[num] > k:
                tracker[nums[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        
        return ans