"""2265. Count Nodes Equal to Average of Subtree"""

"""Problem: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            total_sum = ls + rs + node.val
            total_cnt = lc + rc + 1
            if total_sum // total_cnt == node.val:
                self.count += 1
            return (total_sum, total_cnt)

        dfs(root)
        return self.count