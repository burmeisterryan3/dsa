"""https://leetcode.com/problems/maximum-erasure-value/description/"""

from collections import defaultdict

class Solution:
    def maximum_unique_subarray(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        total = ans = left = 0

        for num in nums:
            freq[num] += 1
            total += num

            while freq[num] > 1:
                total -= nums[left]
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, total)
        
        return ans

    def maximum_unique_subarray_set(self, nums: list[int]) -> int:
        seen = set()
        total = ans = left = 0

        for num in nums:
            if num in seen:
                while nums[left] != num:
                    seen.remove(nums[left])
                    total -= nums[left]
                    left += 1
                left += 1
            else:
                seen.add(num)
                total += num
                ans = max(ans, total)
        
        return ans