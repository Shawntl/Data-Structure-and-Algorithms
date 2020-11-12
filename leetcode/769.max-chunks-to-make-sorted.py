#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        current_max = 0
        i = 0
        chunk = []
        while i < len(arr) - 1:
            chunk.append(arr[i])
            current_max = max(current_max, arr[i])
            if current_max < arr[i+1] and len(chunk) == (current_max+1):
                count += 1
            i += 1
        return count + 1
            
# @lc code=end

