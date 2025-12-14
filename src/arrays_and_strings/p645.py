"""https://leetcode.com/problems/set-mismatch/"""

class Solution:
    def find_error_nums(self, nums: list[int]) -> list[int]:
        complete = set(range(1,len(nums)+1))
        duplicate = None

        for num in nums:
            try:
                complete.remove(num)
            except:
                duplicate = num
            
        return [duplicate, complete.pop()]