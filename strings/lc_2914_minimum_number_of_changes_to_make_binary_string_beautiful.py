"""2914. Minimum Number of Changes to make Binary String Beautiful"""

"""Problem: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/"""


class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                count += 1
        return count