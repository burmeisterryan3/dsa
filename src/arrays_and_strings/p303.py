"""https://leetcode.com/problems/range-sum-query-immutable/"""

class Solution(object):

    def __init__(self, nums: list[int]):
        self.nums = nums[0][0]
        self.cumsum = [0] * len(self.nums)
        self.cumsum[0] = self.nums[0]
        for i in range(len(self.nums)):
            self.cumsum[i] = self.nums[i] + self.cumsum[i-1]

    def sum_range(self, left: int, right: int) -> None:
        return self.cumsum[right] - self.cumsum[left] + self.nums[left]