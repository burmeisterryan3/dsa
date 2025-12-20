"""https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/"""

class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        VOWELS = "aeiou" # runs faster than a set
        
        count = 0
        for i in range(k):
            if s[i] in VOWELS:
                count += 1
        
        ans = count
        for i in range(k, len(s)):
            if s[i-k] in VOWELS: # faster than assignment with if else single line
                count -= 1
            if s[i] in VOWELS:
                count += 1
            if count > ans:
                ans = count

        return ans