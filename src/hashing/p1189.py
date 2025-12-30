"""https://leetcode.com/problems/maximum-number-of-balloons/description/"""

class Solution:
    def max_number_of_balloons(self, text: str) -> int:
        tracker = {"b":0,"a": 0,"l":0,"o":0,"n":0}
        for ch in text:
            if ch in tracker:
                tracker[ch] += 1
        
        tracker["l"] //= 2
        tracker["o"] //= 2

        return min(tracker.values())