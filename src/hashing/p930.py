"""https://leetcode.com/problems/binary-subarrays-with-sum/description/"""

class Solution:
    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        ans = total = 0
        freq = {0:1}

        for num in nums:
            total += num
            ans += freq.get(total-goal, 0)
            freq[total] = freq.get(total, 0) + 1
        
        return ans