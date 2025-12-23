"""https://leetcode.com/problems/find-the-highest-altitude/"""

class Solution:
    def largest_altitude(self, gain: list[int]) -> int:
        largest = window = 0
        for i in range(len(gain)):
            window += gain[i]
            largest = max(largest, window)
        
        return largest