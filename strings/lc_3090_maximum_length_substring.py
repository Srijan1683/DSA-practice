"""3090. Maximum Length Substring with Two Occurrences"""

"""Problem: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/"""


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        ans = 0

        for right, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            while freq[c] > 2:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans