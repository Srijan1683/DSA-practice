"""1111. Maximum Nesting Depth of Two Valid Parentheses Strings"""

"""Problem: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/"""


class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = []
        depth = 0

        for c in seq:
            if c == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1

        return ans