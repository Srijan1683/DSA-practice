"""1190. Reverse Substrings Between Each Pair of Parentheses"""

"""Problem: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/"""


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)

        return ''.join(stack)