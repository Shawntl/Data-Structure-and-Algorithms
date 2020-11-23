#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if ord(target) < ord(letters[left]) or ord(target) >= ord(letters[right]):
            return letters[left]
        
        while left <= right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid - 1
            else:
                left = mid + 1
        return letters[left]
        
# @lc code=end

