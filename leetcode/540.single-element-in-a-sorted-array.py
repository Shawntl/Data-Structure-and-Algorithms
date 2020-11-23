#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            condition1 = (nums[mid] == nums[mid - 1] and mid%2 == 0)
            condition2 = (nums[mid] == nums[mid + 1] and mid%2 != 0)

            condition3 = (nums[mid] == nums[mid - 1] and mid%2 != 0)
            condition4 = (nums[mid] == nums[mid + 1] and mid%2 == 0)
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            elif condition1 or condition2:
                right = mid - 1
            elif condition3 or condition4:
                left = mid + 1
        return nums[left]

        
        
# @lc code=end

