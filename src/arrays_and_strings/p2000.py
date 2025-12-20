"""https://leetcode.com/problems/reverse-prefix-of-word/"""

class Solution(object):
    # def reverse_prefix(self, word: str, ch: str) -> str:
    #     if ch not in word:
    #     s = list(word)

    #     for letter in word:
    #         if lett

    def reverse_prefix_pythonic(self, word: str, ch: str) -> str:
        right = word.find(ch)
        s = list(word)
        left = 0
        while left < right:
            s[right], s[left] = s[left], s[right]
            right -= 1
            left += 1
        return "".join(s)