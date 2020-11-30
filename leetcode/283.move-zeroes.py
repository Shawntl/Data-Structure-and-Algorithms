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
        for i in nums:
            if i != 0:
                nums[idx] = i
                idx += 1
        for j in range(idx, len(nums)):
            nums[j] = 0
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

