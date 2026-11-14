"""3364. Minimum Positive Sum Subarray"""

"""Problem: https://leetcode.com/problems/minimum-positive-sum-subarray/"""


class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        best = float('inf')
        for i in range(n):
            for size in range(l, r + 1):
                j = i + size
                if j > n:
                    break
                s = pre[j] - pre[i]
                if s > 0 and s < best:
                    best = s

        return best if best != float('inf') else -1