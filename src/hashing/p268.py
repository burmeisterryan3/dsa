"""https://leetcode.com/problems/missing-number/description/"""

class Solution:
    def missing_number_option_1(self, nums: list[int]) -> int:
        n = len(nums)
        full_set = set(range(n+1))
        for num in nums:
            full_set.discard(num)
        return full_set.pop()
    
    def missing_number_option_2(self, nums: list[int]) -> int:
        n = len(nums)
        full_set = set(range(n+1))
        nums = set(nums)
        return (full_set-nums).pop()
    
    def missing_number_better_1(self, nums: list[int]) -> int:
        # n*(n+1) // 2 is the sum of numbers 1 to n
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def missing_number_better_2(self, nums: list[int]) -> int:
        # x ^ y ^ y = x
        val = 0
        for i in range(len(nums) + 1):
            val ^= i
        for n in nums:
            val ^= n
        return val