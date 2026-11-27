"""3360. Stone Removal Game"""

"""Problem: https://leetcode.com/problems/stone-removal-game/description/"""


class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        take = 10
        alice_turn = True

        while take > 0 and n >= take:
            n -= take
            take -= 1
            alice_turn = not alice_turn

        return not alice_turn