#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums) -> int:
        max_length = 1
        for i in range(len(nums)):
            s = []
            index = i
            while nums[index] != -1:
                j = index
                s.append(nums[index])
                index = s[-1]
                nums[j] = -1
            max_length = max(max_length, len(s))
        return max_length
# @lc code=end

