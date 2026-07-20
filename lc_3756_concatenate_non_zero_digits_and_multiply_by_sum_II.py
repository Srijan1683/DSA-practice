"""3756. Concatenate Non-Zero Digits and Multiply by Sum II"""

"""Problem: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/description/"""

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)

        prefix_sum = [0] * (n + 1)
        prefix_x = [0] * (n + 1)
        prefix_len = [0] * (n + 1)

        for i, c in enumerate(s):
            d = int(c)
            prefix_sum[i+1] = (prefix_sum[i] + (d if d != 0 else 0)) % MOD
            prefix_len[i+1] = prefix_len[i] + (1 if d != 0 else 0)
            prefix_x[i+1] = (prefix_x[i] * (10 if d != 0 else 1) + (d if d != 0 else 0)) % MOD

        ans = []
        for l, r in queries:
            cnt = prefix_len[r+1] - prefix_len[l]
            if cnt == 0:
                ans.append(0)
                continue
            x = (prefix_x[r+1] - prefix_x[l] * pow(10, cnt, MOD)) % MOD
            total = (prefix_sum[r+1] - prefix_sum[l]) % MOD
            ans.append(x * total % MOD)

        return ans