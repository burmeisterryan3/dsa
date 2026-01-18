"""https://leetcode.com/problems/permutation-in-string/description/"""

from collections import Counter, defaultdict

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        s1_freq, s2_freq = defaultdict(int), defaultdict(int)

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1
        
        if s1_freq == s2_freq:
            return True
        
        left = 0
        for i in range(len(s1), len(s2)):
            s2_freq[s2[i]] += 1
            s2_freq[s2[left]] -= 1

            if s2_freq[s2[left]] == 0:
                del s2_freq[s2[left]]
            
            if s1_freq == s2_freq:
                return True
            
            left += 1

        return False

    def check_inclusion_counter(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s2_freq = Counter(s2[:len(s1)])

        if s1_freq == s2_freq:
            return True
        
        for i in range(len(s1), len(s2)):
            s2_freq[s2[i]] += 1
            s2_freq[s2[i-len(s1)]] -= 1            
            if s1_freq == s2_freq:
                return True

        return False
            
