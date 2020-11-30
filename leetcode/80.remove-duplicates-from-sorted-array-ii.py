#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        flag = True
        slower, faster = 0, 1
        while faster < len(nums):
            if nums[faster] == nums[slower] and flag:
                nums[faster], nums[slower+1] = nums[slower+1], nums[faster]
                slower += 1
                flag = False
            elif nums[faster] > nums[slower]:
                nums[faster], nums[slower+1] = nums[slower+1], nums[faster]
                flag = True
                slower += 1
            faster += 1
        return slower+1
# @lc code=end

