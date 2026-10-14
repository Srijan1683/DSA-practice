"""3723. Maximise Sum of Squares of Digits"""

"""Problem: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/"""


class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        res = "9" * q
        if r:
            res += str(r)
        res += "0" * (num - len(res))
        return res