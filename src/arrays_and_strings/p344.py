"""https://leetcode.com/problems/reverse-string/description/"""

class Solution:
    def reverse_string(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        self.solution = s