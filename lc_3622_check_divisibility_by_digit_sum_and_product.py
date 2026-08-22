"""3622. Check Divisibility by Digit Sum and Product"""

"""Problem: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/?envType=daily-question&envId=2026-08-22"""


class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = [int(d) for d in str(n)]
        total = sum(digits)
        product = 1
        for d in digits:
            product *= d
        return n % (total + product) == 0