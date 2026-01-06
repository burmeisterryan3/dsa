"""https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"""

from collections import defaultdict

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        ans = curr = 0
        tracker = defaultdict(int)
        for i, ch in enumerate(s):
            if ch in tracker:
                ans = max(ans, i - curr) # Find the length between 0 or the last double observed and the current index
                curr = max(curr, tracker[ch] + 1) # Last time we saw letter may be prior to another double (e.g., abba)
            tracker[ch] = i

        return len(s) if ans == 0 else max(ans, len(s)-curr)
    
    def length_of_longest_substring_window(self, s: str) -> int:
        ans = left = 0
        tracker = set()
        for right in range(len(s)):
            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1

            tracker.add(s[right])
            ans = max(ans, right-left+1)

        return ans