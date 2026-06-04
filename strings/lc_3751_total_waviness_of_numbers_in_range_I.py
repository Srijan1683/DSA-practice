"""3751. Total Waviness of Numbers in Range I"""

"""Problem: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/"""

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(n):
            d = [int(c) for c in str(n)]
            if len(d) < 3:
                return 0
            count = 0

            for i in range(1, len(d) - 1):
                if d[i] > d[i-1] and d[i] > d[i+1]:
                    count += 1
                elif d[i] < d[i-1] and d[i] < d[i+1]:
                    count += 1

            return count

        return sum(waviness(n) for n in range(num1, num2 + 1)) 