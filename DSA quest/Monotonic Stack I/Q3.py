"""Largest Rectangle in Histogram"""

"""Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/description/"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hs = heights + [0]
        stack = []
        best = 0

        for i, h in enumerate(hs):
            while stack and hs[stack[-1]] > h:
                height = hs[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                best = max(best, height * width)
            stack.append(i)

        return best