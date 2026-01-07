"""https://leetcode.com/problems/sort-characters-by-frequency/description/"""

from collections import Counter

class Solution:
    def frequency_sort(self, s: str) -> str:
        counts = Counter(s)
        sorted_dict = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

        sorted_string = ""
        for k,v in sorted_dict.items():
            sorted_string += k*v
        
        return sorted_string