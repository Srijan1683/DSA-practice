"""3336. Find the number of subsequences with equal gcd"""

class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = defaultdict(int)
        dp[(0, 0)] = 1

        for x in nums:
            new_dp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD
                new_g1 = gcd(g1, x) if g1 != 0 else x
                new_dp[(new_g1, g2)] = (new_dp[(new_g1, g2)] + cnt) % MOD
                new_g2 = gcd(g2, x) if g2 != 0 else x
                new_dp[(g1, new_g2)] = (new_dp[(g1, new_g2)] + cnt) % MOD
            dp = new_dp

        return sum(cnt for (g1, g2), cnt in dp.items() if g1 == g2 and g1 != 0) % MOD