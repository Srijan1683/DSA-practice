"""1288. Remove Covered Intervals"""

"""Problem: https://leetcode.com/problems/remove-covered-intervals/description/"""

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_right = 0
        for l, r in intervals:
            if r > max_right:
                count += 1
                max_right = r
        return count