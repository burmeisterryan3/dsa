"""https://leetcode.com/problems/find-pivot-index/description/"""

class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        left_sum = right_sum = 0
        for i in range(len(nums)):
            left_sum = nums[i-1] if i > 0 else 0
            right_sum = nums[-1]-nums[i] if i < len(nums)-1 else 0
            if left_sum == right_sum:
                return i
        
        return -1

    def pivot_index_better(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        
        return -1