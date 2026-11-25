"""3411. Maximum Subarray with Equal Products"""

"""Problem: https://leetcode.com/problems/maximum-subarray-with-equal-products/description/"""


class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a

        n = len(nums)
        best = 0
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = l * nums[j] // gcd(l, nums[j])
                if p == g * l:
                    best = max(best, j - i + 1)
        return best