"""https://leetcode.com/problems/path-crossing/"""

class Solution:
    def is_path_crossing(self, path: str) -> bool:
        x = y = 0
        tracker = {(x,y)}
        for step in path:
            if step == "N":
                y += 1
            elif step == "S":
                y -= 1
            elif step == "E":
                x += 1
            else: # step is "W"
                x -= 1

            if (x,y) in tracker:
                return True
            tracker.add((x,y))
        
        return False