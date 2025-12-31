"""https://leetcode.com/problems/jewels-and-stones/description/"""

from collections import defaultdict

class Solution:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        acc = defaultdict(int)
        for stone in stones:
            if stone in jewels:
                acc[stone] += 1
        
        return sum(acc.values())

    def num_jewels_in_stones_pythonic(self, jewels: str, stones: str) -> int:
        acc = 0
        for jewel in jewels:
            acc += stones.count(jewel)
        
        return acc