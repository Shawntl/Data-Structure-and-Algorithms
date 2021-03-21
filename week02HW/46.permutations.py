#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def bracktrack(nums, permutes):
            if len(permutes) == n:
                res.append(permutes)
                return
            for j in range(len(nums)):
                cur_nums = nums[:j]+nums[j+1:]
                bracktrack(cur_nums, permutes+[nums[j]])
        bracktrack(nums, [])
        return res

        
# @lc code=end

