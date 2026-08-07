"""3517. Smallest Palindromic Rearrangement I"""

"""Problem: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/"""

from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        half = []
        mid = ''

        for c in 'abcdefghijklmnopqrstuvwxyz':
            if freq[c] % 2 == 1:
                mid = c
            half.append(c * (freq[c] // 2))

        half = ''.join(half)
        return half + mid + half[::-1]