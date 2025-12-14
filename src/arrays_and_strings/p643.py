"""https://leetcode.com/problems/maximum-average-subarray-i/description/"""

class Solution:
    def find_max_average(self, nums: list[int], k: int) -> float:
        ans = curr = sum(nums[0:k])

        for right in range(k, len(nums)):
            curr += nums[right] - nums[right-k]
            ans = max(ans, curr)

        return ans / k