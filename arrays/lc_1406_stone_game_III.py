"""1406. Stone Game III"""

"""Problem: https://leetcode.com/problems/stone-game-iii/description/"""

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            best = float('-inf')
            total = 0
            for k in range(1,4):
                if (i + k) > n:
                    break
                total += stoneValue[i + k - 1]
                best = max(best, total - dp[i+k])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"            
        
        return "Tie"