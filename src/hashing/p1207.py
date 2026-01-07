"""https://leetcode.com/problems/unique-number-of-occurrences/description/"""

from collections import defaultdict

class Solution:
    def unique_occurrences(self, arr: list[int]) -> bool:
        tracker = defaultdict(int)
        for num in arr:
            tracker[num] += 1
        
        return len(tracker) == len(set(tracker.values()))