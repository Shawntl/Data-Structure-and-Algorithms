#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0]*1001
        res = []
        for num1 in arr1:
            cnt[num1] += 1

        for num2 in arr2:
            res.extend([num2]*cnt[num2])
            cnt[num2] = 0

        for i in range(1001):
            if cnt[i] != 0:
                res.extend([i]*cnt[i])

        return res     
# @lc code=end

