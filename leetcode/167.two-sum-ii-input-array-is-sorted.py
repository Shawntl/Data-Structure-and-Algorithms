#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution one(hash  table)
        # num_dict = {}
        # for i in range(len(numbers)):
        #     first = target - numbers[i]
        #     if first in num_dict.keys():
        #         return [num_dict[first], i+1]
        #     else:
        #         num_dict[numbers[i]] = i + 1
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return
# @lc code=end

