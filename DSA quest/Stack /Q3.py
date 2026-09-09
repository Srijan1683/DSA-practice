"""Exclusive time of Functions"""

"""Problem: https://leetcode.com/problems/exclusive-time-of-functions/description/"""


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid, typ, time = log.split(':')
            fid, time = int(fid), int(time)

            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:
                res[stack[-1]] += time - prev_time + 1
                stack.pop()
                prev_time = time + 1

        return res