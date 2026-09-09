"""Final Prices with a Special Discount in a Shop"""

"""Problem: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/"""


class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        answer = prices[:]
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                answer[j] = prices[j] - prices[i]
            stack.append(i)

        return answer