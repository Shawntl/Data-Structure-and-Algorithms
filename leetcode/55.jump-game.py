#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endReachable = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= endReachable:
                endReachable = i
        return endReachable == 0
        
# @lc code=end

