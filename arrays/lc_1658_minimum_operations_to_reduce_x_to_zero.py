"""1658. Minimum Operations to reduce X to Zero"""

"""Problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/"""


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        left = 0
        curr = 0
        best = -1

        for right in range(len(nums)):
            curr += nums[right]

            while left <= right and curr > target:
                curr -= nums[left]
                left += 1

            if curr == target:
                best = max(best, right - left + 1)

        return len(nums) - best if best != -1 else -1