"""3345. Smallest Divisible Digit Product I"""

"""Problem: https://leetcode.com/problems/smallest-divisible-digit-product-i/description/"""


class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        i = n
        while True:
            product = 1
            for d in str(i):
                product *= int(d)
            if product % t == 0:
                return i
            
            i += 1