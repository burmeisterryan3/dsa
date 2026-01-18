"""https://leetcode.com/problems/custom-sort-string/description/"""

from functools import cmp_to_key
from collections import defaultdict

class Solution:
    def custom_sort_string(self, order: str, s: str) -> str:
        s_map = defaultdict(int)
        for ch in s:
            s_map[ch] += 1
        
        ans = []
        for ch in order:
            if ch in s_map:
                for _ in range(s_map[ch]):
                    ans.append(ch)
                del s_map[ch]

        for ch in s_map:
            for _ in range(s_map[ch]):
                ans.append(ch)
        
        return "".join(ans)

    def custom_sort_string_compare(self, order: str, s: str) -> str:
        rel_value = defaultdict(int)

        def custom_compare(a, b):
            if rel_value[a] < rel_value[b]:
                return -1
            else:
                return 1

        for i, ch in enumerate(order):
            rel_value[ch] = i
        
        return "".join(sorted(s, key=cmp_to_key(custom_compare)))
