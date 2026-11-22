"""2124. Check if all A's appear before all B's"""

"""Problem: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/"""


class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "ba" not in s