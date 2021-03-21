#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, res = [], []
        for i in range(len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            if i - deque[0] > k-1:
                deque.pop(0)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res

        
# @lc code=end

