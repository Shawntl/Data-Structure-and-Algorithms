#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
    # def  moveZeroes(self, nums: List[int]) -> None:
    #     slower, faster = 0, 0
    #     while faster < len(nums):
    #         if nums[slower] != 0:
    #             slower += 1
    #         elif nums[faster] != 0:
    #             nums[faster], nums[slower] = nums[slower], nums[faster]
    #             slower += 1
    #         faster += 1

# @lc code=end

