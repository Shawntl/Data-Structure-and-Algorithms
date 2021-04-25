#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_Rpairs(nums)

    def merge_Rpairs(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        left_cnt = self.merge_Rpairs(left)
        right_cnt = self.merge_Rpairs(right)
        merge_cnt = self.merge(left, right, nums)

        return left_cnt + right_cnt + merge_cnt
    
    def merge(self, left, right, nums):
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[i+j] = left[i]
                i += 1
            else:
                nums[i+j] = right[j]
                j += 1
        if i == len(left):
            nums[i+j:] = right[j:]
        else:
            nums[i+j:] = left[i:]
        ii = jj = 0
        cnt = 0
        while ii < len(left) and jj < len(right):
            if left[ii] <= 2*right[jj]:
                ii += 1
            else:
                cnt += (len(left) - ii)
                jj += 1
        return cnt
        
# @lc code=end

