"""1882. Process Tasks using Servers"""

"""Problem: https://leetcode.com/problems/process-tasks-using-servers/description/"""


import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        t = 0

        for j, dur in enumerate(tasks):
            t = max(t, j)
            if not free and busy[0][0] > t:
                t = busy[0][0]
            while busy and busy[0][0] <= t:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (t + dur, w, i))

        return ans