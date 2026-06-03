"""Find all Numbers Disappeared in an Array"""

"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"""

class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res