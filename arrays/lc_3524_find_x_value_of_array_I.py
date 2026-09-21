"""3524. Find X Value of Array I"""

"""Problem: https://leetcode.com/problems/find-x-value-of-array-i/description/"""


class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            new = [0] * k
            new[x] += 1

            for r in range(k):
                if dp[r]:
                    new[(r * x) % k] += dp[r]

            dp = new

            for r in range(k):
                result[r] += dp[r]

        return result