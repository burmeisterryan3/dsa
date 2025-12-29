"""https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/"""

class Solution:
    def check_if_pangram(self, sentence: str) -> bool:
        letters = set()
        sentence = set(sentence)
        
        for letter in sentence:
            if letter not in letters:
                letters.add(letter)
                if len(letters) == 26: # 26 letters in the English language
                    return True

        return False
        
         