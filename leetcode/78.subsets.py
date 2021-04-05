#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(j, k, subsets):
            if k == 0:
                res.append(subsets)
                return
           
            backtrack(j+1, k-1, subsets+[nums[j]])
            backtrack(j+1, k-1, subsets+[])
        backtrack(0, n, [])
        return res
# @lc code=end

