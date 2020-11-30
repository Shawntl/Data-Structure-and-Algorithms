#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            length = right - left
            width = min(height[left], height[right])
            max_area = max(length*width, max_area)
            if width == height[left]:
                while height[left] <= width and left < right:
                    left += 1
            else:
                while height[right] <= width and left < right:
                    right -= 1
        return max_area

       
# @lc code=end

