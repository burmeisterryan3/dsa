"""https://leetcode.com/problems/move-zeroes/"""

class Solution:
    def move_zeros(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        
        while right < len(nums) and nums[right] != 0:
            right += 1
            left += 1

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums