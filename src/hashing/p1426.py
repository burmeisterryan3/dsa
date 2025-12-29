"""https://leetcode.com/problems/counting-elements/"""

class Solution:
    def count_elements(self, arr: list[int]) -> int:
        ans = 0
        tracker = set(arr)
        for num in arr:
            if num+1 in tracker:
                ans += 1
        return ans