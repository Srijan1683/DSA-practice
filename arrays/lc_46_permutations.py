"""46. Permutations"""

"""Problem: https://leetcode.com/problems/permutations/description/"""

"""Approach: use backtracking to explore every number in path and compare the length of path with nums to save 1 copy of permutation"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []

        def backtrack():
            if len(nums)==len(path):
                result.append(path[:])

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack()
                path.pop()

        backtrack()
        return result