"""2574. Left and Right Sum Differences"""

"""Problem: https://leetcode.com/problems/left-and-right-sum-differences/"""

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left, right = 0, sum(nums)
        ans = []

        for x in nums:
            right -= x
            ans.append(abs(left - right))
            left += x

        return ans