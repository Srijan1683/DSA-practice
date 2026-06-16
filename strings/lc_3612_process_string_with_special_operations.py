"""3612: Process String with Special Operations I"""

"""Problem: https://leetcode.com/problems/process-string-with-special-operations-i/"""


class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in s:
            if c.islower():
                result.append(c)
            elif c == '*':
                if result:
                    result.pop()
            elif c == '#':
                result += result[:]
            elif c == '%':
                result.reverse()
        return ''.join(result)