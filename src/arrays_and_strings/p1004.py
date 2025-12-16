"""https://leetcode.com/problems/max-consecutive-ones-iii/"""

class Solution:
    def longest_ones(self, nums: list[int], k: int) -> int:
        if set(nums) == {0}:
            return k

        left = ans = num_zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            
            ans = max(ans, right-left+1)

        return ans