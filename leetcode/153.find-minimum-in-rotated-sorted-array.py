#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if (nums[0] < nums[1]) and (nums[0] < nums[-1]):
            return nums[0]
        if (nums[-1] < nums[-2]) and (nums[-1] < nums[0]):
            return nums[-1]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (nums[mid] < nums[mid-1]) and (nums[mid] < nums[mid+1]):
                return nums[mid]
            elif (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                return nums[mid + 1]
            elif nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] > nums[left]:
                left = mid + 1
        return

        
# @lc code=end

