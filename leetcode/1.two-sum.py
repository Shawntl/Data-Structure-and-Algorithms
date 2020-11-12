#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0, len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

# @lc code=end

