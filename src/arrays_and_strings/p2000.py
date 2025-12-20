"""https://leetcode.com/problems/reverse-prefix-of-word/"""

class Solution(object):
    def reverse_prefix(self, word: str, ch: str) -> str:
        left = right = 0
        while word[right] != ch:
            right += 1
            if right == len(word):
                return word
        
        s = list(word)
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
        
        return "".join(s)


    def reverse_prefix_pythonic(self, word: str, ch: str) -> str:
        right = word.find(ch)
        s = list(word)
        left = 0
        while left < right:
            s[right], s[left] = s[left], s[right]
            right -= 1
            left += 1
        return "".join(s)