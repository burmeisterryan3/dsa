"""https://leetcode.com/problems/word-pattern/description/"""

class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        sp_map = {}
        for p_ch, s_word in zip(pattern, s.split()):
            if p_ch in sp_map:
                if sp_map[p_ch] != s_word:
                    return False
            else:
                if s_word in sp_map.values():
                    return False
                sp_map[p_ch] = s_word
        
        return True