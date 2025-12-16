"""https://leetcode.com/problems/k-radius-subarray-averages/description/"""

class Solution:
    def get_averages(self, nums: list[int], k: int) -> list[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = [-1]*len(nums)

        denominator = 2*k + 1
        for i in range(k, len(nums)-k):
            ans[i] = (prefix[i+k] - prefix[i-k] + nums[i-k]) // denominator

        return ans
    
    def get_averages_better(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums

        ans = [-1]*len(nums)
        window_size = 2*k + 1
        
        if window_size > len(nums):
            return ans

        window_sum = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            # Subtract sum of the points preceding the window's left bound
            if i >= window_size:
                window_sum -= nums[i-window_size]
            
            if i >= window_size - 1:
                ans[i-k] = window_sum // window_size

        return ans