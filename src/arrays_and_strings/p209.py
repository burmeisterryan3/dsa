"""https://leetcode.com/problems/minimum-size-subarray-sum/description/"""

class Solution:
    def min_sub_array_len(self, target: int, nums: list[int]) -> int:
        left = total = 0
        ans = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(right-left+1, ans)
                total -= nums[left]
                left += 1
        
        return ans if ans <= len(nums) else 0
        