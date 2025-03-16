#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        backup_dict = {}
        for i, num in enumerate(nums):
            if target - num in backup_dict:
                return [backup_dict[target - num], i]
            else:
                backup_dict[num] = i
        
# @lc code=end

