"""2948. Make Lexicographically Smallest Array by Swapping Elements"""

"""Problem: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/"""


class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        sorted_pairs = sorted(enumerate(nums), key=lambda x: x[1])

        result = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and sorted_pairs[j+1][1] - sorted_pairs[j][1] <= limit:
                j += 1

            group_indices = [sorted_pairs[k][0] for k in range(i, j+1)]
            group_vals = [sorted_pairs[k][1] for k in range(i, j+1)]

            for idx, val in zip(sorted(group_indices), group_vals):
                result[idx] = val

            i = j + 1

        return result