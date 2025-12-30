"""https://leetcode.com/problems/contiguous-array/"""

from collections import defaultdict

class Solution:
    def find_max_length(self, nums: list[int]) -> int:
        tracker = defaultdict(lambda: -1)
        ans = curr = 0
        for i, num in enumerate(nums):
            if num == 0:
                curr -= 1
            else:
                curr += 1

            if curr == 0:
                ans = i+1
            elif tracker[curr] >= 0:
                ans = max(ans, i-tracker[curr])
            else:
                tracker[curr] = i
       
        return ans

    def find_max_length_better(self, nums: list[int]) -> int:
        # First = prefix sum & will track the index where we first see a sum
        # Logic:  If we see the sum again, an equal number of 0s and 1s have appeared
        first = {0: -1}
        ans = running_sum = 0
        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in first:
                ans = max(ans, i-first[running_sum])
            else:
                first[running_sum] = i
       
        return ans