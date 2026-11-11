"""3789. Minimum Cost to Acquire Required Items"""

"""Problem: https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/"""


class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        def f(b):
            return b * costBoth + max(0, need1 - b) * cost1 + max(0, need2 - b) * cost2

        return min(f(0), f(need1), f(need2))