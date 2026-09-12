"""3483. Unique 3-Digit Even Numbers"""

"""https://leetcode.com/problems/unique-3-digit-even-numbers/description/"""


class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        n = len(digits)
        seen = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0:
                        seen.add((digits[i], digits[j], digits[k]))
        return len(seen)