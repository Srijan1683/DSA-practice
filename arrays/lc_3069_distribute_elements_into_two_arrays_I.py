"""3069. Distribute Elements into Two Arrays I"""

"""Problem: https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/"""


class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2