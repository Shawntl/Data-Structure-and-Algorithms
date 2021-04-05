#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxdp = [nums[0]]+[float('-inf')]*(len(nums)-1)
        mindp = [nums[0]]+[float('inf')]*(len(nums)-1)
        for i in range(1, len(nums)):
            maxdp[i] = max(nums[i]*maxdp[i-1], 
                           nums[i]*mindp[i-1],
                           nums[i])
            mindp[i] = min(nums[i]*maxdp[i-1], 
                           nums[i]*mindp[i-1],
                           nums[i])
        return max(maxdp)
        
# @lc code=end

