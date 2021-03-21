#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, k, cbs):
            if k == 0:
                res.append(cbs)
                return
            for j in range(i, n+1):
                backtrack(j+1, k-1, cbs+[j])
        backtrack(1, k, [])
        return res


        
# @lc code=end

