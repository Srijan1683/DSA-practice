"""1524. Number of Subarray with Odd Sum"""

"""Problem: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/"""


class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        even, odd = 1, 0
        parity = 0
        ans = 0

        for x in arr:
            parity ^= x & 1
            if parity:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD