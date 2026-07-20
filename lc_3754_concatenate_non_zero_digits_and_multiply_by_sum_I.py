"""3754. Concatenate Non-Zero Digits and Multiply by Sum I"""

"""Problem: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/description/"""

class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [c for c in str(n) if c != '0']
        if not digits:
            return 0
        x = int(''.join(digits))
        return x * sum(int(d) for d in digits)