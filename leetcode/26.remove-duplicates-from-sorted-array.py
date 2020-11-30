#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        slower, faster = 0, 1
        while faster < len(nums):
            if nums[faster] > nums[slower]:
                nums[slower+1], nums[faster] = nums[faster], nums[slower+1]
                slower += 1
            faster += 1
        return slower + 1
            

   
# @lc code=end

