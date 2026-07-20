"""1331. Rank Transform Of An Array"""

"""Problem: https://leetcode.com/problems/rank-transform-of-an-array/description/"""

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [rank[v] for v in arr]