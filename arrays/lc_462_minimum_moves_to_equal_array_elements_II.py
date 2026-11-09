"""462. Minimum Moves to Equal Array Elements II"""

"""Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/"""


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)