"""https://leetcode.com/problems/counting-elements/"""

from collections import defaultdict, Counter

class Solution:
    def find_lucky(self, arr: list[int]) -> int:
        counts = defaultdict(int)
        lucky = set()
        for num in arr:
            counts[num] += 1
            if num in lucky:
                lucky.remove(num)
            if counts[num] == num:
                lucky.add(num)
        
        if len(lucky) == 0:
            return -1
        else:
            return max(lucky)

    def find_lucky_counter(self, arr: list[int]) -> int:
        counts = Counter(arr)
        res = -1

        for k,v in counts.items():
            if k == v:
                res = max(res, k)

        return res