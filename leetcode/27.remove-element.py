#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        slower, faster = 0, 0
        while faster < len(nums):
            if nums[slower] != val:
                slower += 1
            elif nums[faster] != val:
                nums[faster], nums[slower] = nums[slower], nums[faster]
                slower += 1
            faster += 1
        return slower
# @lc code=end

