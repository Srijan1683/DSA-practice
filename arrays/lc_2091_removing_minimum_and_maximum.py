"""2091. Removing Minimum and Maximum from an Array"""

"""Problem: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/"""


class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        return min((max(min_idx, max_idx) + 1),
        (len(nums) - min(min_idx, max_idx)),
        (min(min_idx, max_idx) + 1) + (len(nums) - max(min_idx, max_idx)))