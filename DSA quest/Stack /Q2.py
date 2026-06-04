"""Evaluate Reverse Polish Notion"""

"""Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/"""


from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a, 
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(b / a)  # Use float division then truncate
        }

        for token in tokens:
            if token in operations:
                val1 = stack.pop()
                val2 = stack.pop()
                result = operations[token](val1, val2)
                stack.append(result)
            else:
                stack.append(int(token))
                
        return stack[0]