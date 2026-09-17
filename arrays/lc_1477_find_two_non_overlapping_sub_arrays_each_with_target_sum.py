"""1477. Find Two Non-Overlapping Sub Arrays each with Target Sum"""

"""Problem: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/"""


class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')
        best = [INF] * n
        ans = INF
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target:
                cur_sum -= arr[left]
                left += 1

            if cur_sum == target:
                cur_len = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, cur_len + best[left - 1])
                best[right] = min(best[right - 1] if right > 0 else INF, cur_len)
            else:
                best[right] = best[right - 1] if right > 0 else INF

        return ans if ans != INF else -1