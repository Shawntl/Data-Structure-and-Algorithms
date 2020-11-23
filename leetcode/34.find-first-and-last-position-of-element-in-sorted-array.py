#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left1, right1 = 0, len(nums) - 1
        while left1 <= right1:
            mid = (left1 + right1) // 2
            if nums[mid] >= target:
                right1 = mid - 1
            else:
                left1 = mid + 1
        start = left1

        left2, right2 = 0, len(nums) - 1
        while left2 <= right2:
            mid = (left2 + right2) // 2
            if nums[mid] <= target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        end = right2
        if start > (len(nums)-1) or end < 0:
            return [-1, -1]
        elif nums[start] == nums[end] == target:
            return [start, end]
        else:
            return [-1, -1]
        
# @lc code=end

