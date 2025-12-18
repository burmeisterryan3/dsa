"""https://leetcode.com/problems/reverse-only-letters/"""

class Solution:
    def reverse_only_letters(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)

        while left < right:
            while left < len(s) and not s[left].isalpha():
                left += 1
            
            while right >= 0 and not s[right].isalpha():
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                    
        return "".join(s)