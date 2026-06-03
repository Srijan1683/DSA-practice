"""Build an Array with Stack operations"""

"""Problem: https://leetcode.com/problems/build-an-array-with-stack-operations/"""

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        arr = []

        for i in range (1,n+1):
            if i in target:
                arr.append("Push")
            else:
                if i <= target[-1]: 
                    arr.append("Push")
                    arr.append("Pop")
                else:
                    continue
        return arr