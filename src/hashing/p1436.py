"""https://leetcode.com/problems/destination-city/"""

class Solution:
    def dest_city(self, paths: list[list[str]]) -> str:
        dests = set()
        sources = set()
        for path in paths:
            sources.add(path[0])
            dests.add(path[1])
        
        return (dests-sources).pop()