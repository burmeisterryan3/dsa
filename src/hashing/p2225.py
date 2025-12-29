"""https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/"""

from collections import defaultdict

class Solution:
    def find_winners(self, matches: list[list[int]]) -> list[list[int]]:
        tracker = defaultdict(int)

        for winner, loser in matches:
            if winner not in tracker:
                tracker[winner] = 0
            tracker[loser] += 1

        zero_loss = []
        one_loss = []
        for player, losses in tracker.items():
            if losses == 0:
                zero_loss.append(player)
            elif losses == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]