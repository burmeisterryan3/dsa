"""https://leetcode.com/problems/squares-of-a-sorted-array/description/"""

class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        """https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1854735375/"""
        nums = list(map(lambda x: x**2, nums))
        self.solution = sorted(nums)
        return self.solution
    
    def sorted_squares_alt(self, nums: list[int]) -> list[int]:
        """https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1854738761/"""
        left = right = 0

        # Find the first 0 or positive number
        while right < len(nums) and nums[right] < 0:
            right += 1
        # Set a negative negative pointer immediately to the left of the first positive or 0 number
        left = right-1

        self.solution = []
        while left >= 0 and right < len(nums):
            if abs(nums[left]) <= nums[right]:
                self.solution.append(nums[left]**2)
                left -= 1
            else:
                self.solution.append(nums[right]**2)
                right += 1

        while left >= 0:
            self.solution.append(nums[left]**2)
            left -= 1

        while right < len(nums):
            self.solution.append(nums[right]**2)
            right += 1

        return self.solution