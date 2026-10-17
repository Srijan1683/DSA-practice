"""3551. Minimum Swaps to Sort by Digit Sum"""

"""Problem: https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/"""


class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        visited = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if visited[i] or pos[arr[i]] == i:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle += 1

            ans += cycle - 1

        return ans