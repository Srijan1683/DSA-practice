"""1621. Number of Sets of K-Overlapping line segments"""

"""Problem: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/"""


class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        ans = 1

        for i in range(1, 2 * k + 1):
            ans = ans * (n + k - i) % MOD
            ans = ans * pow(i, MOD - 2, MOD) % MOD

        return ans