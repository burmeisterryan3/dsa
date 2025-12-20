"""https://leetcode.com/problems/minimum-common-value/description/"""

class Solution:
    def get_common(self, nums1: list[int], nums2: list[int]) -> int:
        left = right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] > nums2[right]:
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else: # equal
                return nums1[left]
        return -1
            