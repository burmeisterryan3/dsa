"""https://leetcode.com/problems/get-equal-substrings-within-budget/"""

class Solution():
    def equal_substring_speed(self, s:str, t:str, max_cost:int) -> int:
        left = max_length = running_cost = 0
        all_costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(t))]

        for right in range(len(s)):
            running_cost += all_costs[right]
            while running_cost > max_cost:
                running_cost -= all_costs[left]
                left += 1

            max_length = max(right-left+1, max_length)
        return max_length


    def equal_substring_memory(self, s:str, t:str, max_cost:int) -> int:
        left = max_length = cost = 0
        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > max_cost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(right-left+1, max_length)
        return max_length