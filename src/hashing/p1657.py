"""https://leetcode.com/problems/determine-if-two-strings-are-close/description/"""

from collections import Counter

class Solution:
    def close_strings(self, word1: str, word2: str) -> bool:
        w1_counts = Counter(word1)
        w2_counts = Counter(word2)

        return ((w1_counts.keys() == w2_counts.keys()) and
               (sorted(w1_counts.values()) == sorted(w2_counts.values())))