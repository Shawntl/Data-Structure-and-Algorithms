#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s1, s2, end = m-1, n-1, m+n-1
        while s1 >= 0 and s2 >= 0:
            if nums1[s1] >= nums2[s2]:
                nums1[end] = nums1[s1]
                s1 -= 1
            else:
                nums1[end] = nums2[s2]
                s2 -= 1
            end -= 1
        if s2 >= 0:
            nums1[:s2+1] = nums2[:s2+1]
            
# @lc code=end

