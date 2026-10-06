"""921. Minimum Add to make Parentheses Valid"""

"""Problem: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/"""


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open = 0
        ans = 0

        for c in s:
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    ans += 1

        return ans + open