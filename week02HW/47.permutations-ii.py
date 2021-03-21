#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def bracktrack(nums, permutes):
            if len(permutes) == n:
                res.append(permutes)
                return
            check = []
            for j in range(len(nums)):
                if nums[j] not in check:
                    cur_nums = nums[:j]+nums[j+1:]
                    bracktrack(cur_nums, permutes+[nums[j]])
                    check.append(nums[j])
        bracktrack(nums, [])
        return res
        
# @lc code=end

