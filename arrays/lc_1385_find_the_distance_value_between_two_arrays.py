"""1385. Find the Distance Value between Two Arrays"""

"""Problem: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/"""


import bisect
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        count = 0
        for x in arr1:
            i = bisect.bisect_left(arr2, x)
            ok = True
            if i < len(arr2) and arr2[i] - x <= d:
                ok = False
            if i > 0 and x - arr2[i - 1] <= d:
                ok = False
            if ok:
                count += 1
        return count