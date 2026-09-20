"""3498. Reverse Degree of a String"""

"""Problem: https://leetcode.com/problems/reverse-degree-of-a-string/description/"""


class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            ans += value * (i + 1)

        return ans