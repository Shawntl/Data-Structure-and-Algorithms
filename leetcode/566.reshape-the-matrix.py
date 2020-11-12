#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        current_r = len(nums)
        current_c = len(nums[0])
        if (current_r * current_c) != (r * c):
            return nums
        
        first_row = nums[0]
        for i in range(1, len(nums)):
            first_row.extend(nums[i])
        
        result = [first_row[i:i+c] for i in range(0, len(first_row), c)]

        return result
        
# @lc code=end

