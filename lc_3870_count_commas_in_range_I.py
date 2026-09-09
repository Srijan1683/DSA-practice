"""3870. Count Commas in Range I"""

"""Problem: https://leetcode.com/problems/count-commas-in-range/description/"""


class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        d = 1
        while True:
            lo = 1 if d == 1 else 10 ** (d - 1)
            hi = 10 ** d - 1
            if lo > n:
                break
            cnt = min(hi, n) - lo + 1
            total += cnt * ((d - 1) // 3)
            d += 1
        return total