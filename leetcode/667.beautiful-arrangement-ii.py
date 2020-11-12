#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = [1]
        flag = True
        for i in range(k, 0, -1):
            if flag:
                result.append(result[-1] + i)
                flag = False
            else:
                result.append(result[-1] - i)
                flag = True
        for i in range(1 + k + 1, n + 1):
            result.append(i)
        return result
        
# @lc code=end

