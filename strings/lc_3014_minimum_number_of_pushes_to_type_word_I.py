"""3014. Minimum Number of Pushes to type Word I"""

"""Problem: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/"""

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        return sum((i // 8 + 1) for i in range(n))