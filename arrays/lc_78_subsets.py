"""78. Subsets"""

"""Problem: https://leetcode.com/problems/subsets/description/"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def backtrack(index):
            result.append(path[:])

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result