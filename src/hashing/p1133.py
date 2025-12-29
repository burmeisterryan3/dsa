"""https://leetcode.com/problems/largest-unique-number/description/"""

class Solution:
    def largest_unique_number(self, nums: list[int]) -> int:
        tracker = {}
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1
        
        ans = -1
        for num, occurrences in tracker.items():
            if occurrences == 1:
                ans = max(ans, num)

        return ans