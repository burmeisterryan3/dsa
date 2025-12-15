class Solution():
    def min_start_value(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        low = nums[0]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            low = min(low, prefix[-1])

        if low <= 0:
            return abs(low) + 1        
        else:
            return 1