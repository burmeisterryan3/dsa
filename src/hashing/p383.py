"""https://leetcode.com/problems/ransom-note/description/"""

from collections import defaultdict

class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for ch in ransom_note:
            letters[ch] += 1
        
        for ch in magazine:
            if letters[ch] > 0:
                letters[ch] -= 1
                if sum(letters.values()) == 0:
                    return True
        
        return False
    
    def can_construct_pythonic(self, ransom_note: str, magazine: str) -> bool:
        for letter in set(ransom_note):
            if ransom_note.count(letter) > magazine.count(letter):
                return False
        
        return True