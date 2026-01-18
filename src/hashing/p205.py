"""https://leetcode.com/problems/isomorphic-strings/description/"""

class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        st_map = {}
        for s_ch, t_ch in zip(s, t):
            if s_ch in st_map:
                if st_map[s_ch] != t_ch:
                    return False
            else:
                if t_ch in st_map.values():
                    return False
                st_map[s_ch] = t_ch
        
        return True