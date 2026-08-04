"""3731. Find Missing Elements"""

"""Problem: https://leetcode.com/problems/find-missing-elements/description/"""


class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = min(nums)
        b = max(nums)
        nums_set = set(nums)

        result = []

        for i in range(a, b+1):
            if i not in nums_set:
                result.append(i)

        return result