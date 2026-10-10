"""1541. Minimum Insertions to Balance a Parentheses String"""

"""Problem: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/"""


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        open = 0
        ans = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                if open > 0:
                    open -= 1
                else:
                    ans += 1

            i += 1

        return ans + open * 2