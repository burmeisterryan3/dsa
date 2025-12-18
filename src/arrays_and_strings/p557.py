"""https://leetcode.com/problems/reverse-words-in-a-string-iii/description/"""

class Solution:
    def reverse_words(self, s: str) -> str:
        left = 0
        s = list(s + " ")

        for i in range(len(s)):
            if s[i] == " ":
                right = i-1
                while left < right:
                    s[right], s[left] = s[left], s[right]
                    right -= 1
                    left += 1

                left = i+1
                    
        return "".join(s)[:-1]

    def reverse_words_pythonic(self, s: str) -> str:
        words = s.split(" ")
        rev = [word[::-1] for word in words]
        return " ".join(rev)
            