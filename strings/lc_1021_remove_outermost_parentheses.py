"""1021. Remove Outermost Parentheses"""

"""Problem: https://leetcode.com/problems/remove-outermost-parentheses/"""


class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        depth = 0

        for c in s:
            if c == '(':
                if depth > 0:
                    ans.append(c)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans.append(c)

        return ''.join(ans)