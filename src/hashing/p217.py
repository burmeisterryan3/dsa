"""https://leetcode.com/problems/contains-duplicate/description/"""

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        tracker = set()
        for num in nums:
            if num in tracker:
                return True
            tracker.add(num)
        
        return False

    def contains_duplicate_better(self, nums: list[int]) -> bool:
        return len(nums) > len(set(nums))