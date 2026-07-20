"""1291. Sequential Digits"""

"""Problem: https://leetcode.com/problems/sequential-digits/description/"""

class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        for start in range(1,9):
            num = 0
            for d in range(start, 10):
                num = num * 10 + d
                if num > high:
                    break
                if num >= low:
                    result.append(num)

        return sorted(result)