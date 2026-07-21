"""39. Combination Sum"""

"""Problem: https://leetcode.com/problems/combination-sum/description/"""

class Solution:
    def combinationSum(self, candidates, target):
        path = []
        result = []
        
        def backtrack(index, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()
                
        backtrack(0, target)
        return result